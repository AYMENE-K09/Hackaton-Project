from database.index import db

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
