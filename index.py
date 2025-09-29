from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from database.index import init_db, db
from models.library_models import Book, Category, Author, BooksAuthors, Borrowing, User
from datetime import datetime, date
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///library.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

init_db(app)

# Create default admin user if it doesn't exist
def create_default_admin():
    with app.app_context():
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            admin = User(username='admin', email='admin@library.com', is_admin=True)
            admin.set_password('admin123')
            db.session.add(admin)
            
            # Create a regular user for demo
            user = User(username='user', email='user@library.com', is_admin=False)
            user.set_password('user123')
            db.session.add(user)
            
            db.session.commit()
            print("✅ Default users created:")
            print("   Admin: admin / admin123")
            print("   User: user / user123")

create_default_admin()

# Template context processor to make current year and user available in all templates
@app.context_processor
def inject_current_year():
    return {
        'current_year': datetime.now().year,
        'current_user': current_user
    }

# Admin required decorator
def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Admin access required.', 'error')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

# Authentication routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        if not username or not password:
            flash('Please fill in all fields.', 'error')
            return render_template('login.html')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        # Validation
        errors = []
        if not username or len(username) < 3:
            errors.append('Username must be at least 3 characters long.')
        if not email or '@' not in email:
            errors.append('Please enter a valid email address.')
        if not password or len(password) < 6:
            errors.append('Password must be at least 6 characters long.')
        if password != confirm_password:
            errors.append('Passwords do not match.')
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            errors.append('Username already exists.')
        if User.query.filter_by(email=email).first():
            errors.append('Email already registered.')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('register.html')
        
        try:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating account: ' + str(e), 'error')
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('home'))

@app.route('/')
def home():
    # Get search and filter parameters
    search = request.args.get('search', '')
    category_id = request.args.get('category', '')
    
    # Build query
    query = Book.query
    
    if search:
        query = query.filter(Book.title.contains(search))
    
    if category_id:
        query = query.filter(Book.category_id == category_id)
    
    books = query.all()
    categories = Category.query.all()
    
    return render_template('index.html', books=books, categories=categories, 
                         search=search, selected_category=category_id)

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        publication_year = request.form.get('publication_year')
        category_id = request.form.get('category_id')
        author_ids = request.form.getlist('author_ids')

        # Validation
        errors = []
        if not title:
            errors.append('Title is required')
        if not publication_year:
            errors.append('Publication year is required')
        elif not publication_year.isdigit() or int(publication_year) < 1000 or int(publication_year) > datetime.now().year:
            errors.append('Invalid publication year')
        if not category_id:
            errors.append('Category is required')

        if errors:
            for error in errors:
                flash(error, 'error')
            categories = Category.query.all()
            authors = Author.query.all()
            return render_template('create.html', categories=categories, authors=authors)

        try:
            book = Book(
                title=title,
                description=description,
                publication_year=int(publication_year),
                category_id=int(category_id)
            )
            db.session.add(book)
            db.session.flush()  # Get the book ID

            # Add authors
            for author_id in author_ids:
                if author_id:
                    book_author = BooksAuthors(book_id=book.id, author_id=int(author_id))
                    db.session.add(book_author)

            db.session.commit()
            flash('Book created successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating book: ' + str(e), 'error')
    
    categories = Category.query.all()
    authors = Author.query.all()
    return render_template('create.html', categories=categories, authors=authors)

@app.route('/details/<int:id>')
def details(id):
    book = Book.query.get_or_404(id)
    return render_template('details.html', book=book)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    book = Book.query.get_or_404(id)
    
    if request.method == 'POST':
        book.title = request.form.get('title')
        book.description = request.form.get('description')
        book.publication_year = request.form.get('publication_year')
        book.category_id = request.form.get('category_id')
        
        db.session.commit()
        return redirect(url_for('details', id=id))
    
    categories = Category.query.all()
    return render_template('edit.html', book=book, categories=categories)

@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    book = Book.query.get_or_404(id)
    try:
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting book: ' + str(e), 'error')
    return redirect(url_for('home'))

# Authors Management
@app.route('/authors')
def authors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)

@app.route('/authors/create', methods=['GET', 'POST'])
def create_author():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        biography = request.form.get('biography', '').strip()
        birth_year = request.form.get('birth_year')

        errors = []
        if not name:
            errors.append('Name is required')
        if birth_year and (not birth_year.isdigit() or int(birth_year) < 1000 or int(birth_year) > datetime.now().year):
            errors.append('Invalid birth year')

        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('create_author.html')

        try:
            author = Author(
                name=name,
                biography=biography,
                birth_year=int(birth_year) if birth_year else None
            )
            db.session.add(author)
            db.session.commit()
            flash('Author created successfully!', 'success')
            return redirect(url_for('authors'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating author: ' + str(e), 'error')
    
    return render_template('create_author.html')

@app.route('/authors/<int:id>')
def author_details(id):
    author = Author.query.get_or_404(id)
    return render_template('author_details.html', author=author)

# Borrowings Management
@app.route('/borrowings')
def borrowings():
    borrowings = Borrowing.query.all()
    return render_template('borrowings.html', borrowings=borrowings)

@app.route('/borrow/<int:book_id>', methods=['GET', 'POST'])
def borrow_book(book_id):
    book = Book.query.get_or_404(book_id)
    
    if request.method == 'POST':
        borrower_name = request.form.get('borrower_name', '').strip()
        borrow_date = request.form.get('borrow_date')

        errors = []
        if not borrower_name:
            errors.append('Borrower name is required')
        if not borrow_date:
            errors.append('Borrow date is required')

        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('borrow_book.html', book=book)

        try:
            borrowing = Borrowing(
                book_id=book_id,
                borrower_name=borrower_name,
                borrow_date=datetime.strptime(borrow_date, '%Y-%m-%d').date()
            )
            db.session.add(borrowing)
            db.session.commit()
            flash('Book borrowed successfully!', 'success')
            return redirect(url_for('borrowings'))
        except Exception as e:
            db.session.rollback()
            flash('Error borrowing book: ' + str(e), 'error')
    
    return render_template('borrow_book.html', book=book)

@app.route('/return/<int:borrowing_id>', methods=['POST'])
def return_book(borrowing_id):
    borrowing = Borrowing.query.get_or_404(borrowing_id)
    try:
        borrowing.return_date = date.today()
        db.session.commit()
        flash('Book returned successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error returning book: ' + str(e), 'error')
    return redirect(url_for('borrowings'))

# Admin Dashboard
@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    # Get comprehensive statistics
    total_books = Book.query.count()
    total_authors = Author.query.count()
    total_categories = Category.query.count()
    total_users = User.query.count()
    total_borrowings = Borrowing.query.count()
    active_borrowings = Borrowing.query.filter(Borrowing.return_date.is_(None)).count()
    
    # Recent activity
    recent_books = Book.query.order_by(Book.id.desc()).limit(5).all()
    recent_users = User.query.order_by(User.created_at.desc()).limit(5).all()
    recent_borrowings = Borrowing.query.order_by(Borrowing.borrow_date.desc()).limit(5).all()
    
    # Books by category
    books_by_category = db.session.query(Category.name, db.func.count(Book.id)).join(Book).group_by(Category.name).all()
    
    # Most borrowed books
    most_borrowed = db.session.query(Book.title, db.func.count(Borrowing.id)).join(Borrowing).group_by(Book.id, Book.title).order_by(db.func.count(Borrowing.id).desc()).limit(5).all()
    
    return render_template('admin_dashboard.html',
                         total_books=total_books,
                         total_authors=total_authors,
                         total_categories=total_categories,
                         total_users=total_users,
                         total_borrowings=total_borrowings,
                         active_borrowings=active_borrowings,
                         recent_books=recent_books,
                         recent_users=recent_users,
                         recent_borrowings=recent_borrowings,
                         books_by_category=books_by_category,
                         most_borrowed=most_borrowed)

# User Management
@app.route('/admin/users')
@login_required
@admin_required
def admin_users():
    users = User.query.all()
    return render_template('admin_users.html', users=users)

@app.route('/admin/toggle-admin/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def toggle_admin(user_id):
    if user_id == current_user.id:
        flash('You cannot modify your own admin status.', 'error')
        return redirect(url_for('admin_users'))
    
    user = User.query.get_or_404(user_id)
    is_admin = request.form.get('is_admin') == 'True'
    
    try:
        user.is_admin = is_admin
        db.session.commit()
        action = 'granted admin privileges to' if is_admin else 'removed admin privileges from'
        flash(f'Successfully {action} {user.username}.', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error updating user privileges: ' + str(e), 'error')
    
    return redirect(url_for('admin_users'))

# Statistics
@app.route('/stats')
def stats():
    total_books = Book.query.count()
    total_authors = Author.query.count()
    total_categories = Category.query.count()
    total_borrowings = Borrowing.query.count()
    active_borrowings = Borrowing.query.filter(Borrowing.return_date.is_(None)).count()
    
    # Books by category
    books_by_category = db.session.query(Category.name, db.func.count(Book.id)).join(Book).group_by(Category.name).all()
    
    # Most borrowed books
    most_borrowed = db.session.query(Book.title, db.func.count(Borrowing.id)).join(Borrowing).group_by(Book.id, Book.title).order_by(db.func.count(Borrowing.id).desc()).limit(5).all()
    
    return render_template('stats.html', 
                         total_books=total_books,
                         total_authors=total_authors,
                         total_categories=total_categories,
                         total_borrowings=total_borrowings,
                         active_borrowings=active_borrowings,
                         books_by_category=books_by_category,
                         most_borrowed=most_borrowed)

if __name__ == '__main__':
    app.run(debug=True)
