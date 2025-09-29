from database.index import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# جدول المستخدمين
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

# جدول الفئات
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    books = db.relationship('Book', backref='category', lazy=True)

# جدول المؤلفين
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.Text)
    birth_year = db.Column(db.Integer)
    books = db.relationship('BooksAuthors', back_populates='author')

# جدول الكتب
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    publication_year = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    authors = db.relationship('BooksAuthors', back_populates='book')
    borrowings = db.relationship('Borrowing', backref='book', lazy=True)

# جدول العلاقة Many-to-Many
class BooksAuthors(db.Model):
    __tablename__ = 'books_authors'
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), primary_key=True)
    book = db.relationship('Book', back_populates='authors')
    author = db.relationship('Author', back_populates='books')

# جدول الاستعارات
class Borrowing(db.Model):
    __tablename__ = 'borrowings'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    borrower_name = db.Column(db.String(100), nullable=False)
    borrow_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date)
