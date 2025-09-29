# 📚 Library Management System

A modern, full-featured library management system built with Flask and Tailwind CSS. This system provides comprehensive book management, author tracking, borrowing functionality, and detailed statistics.

## ✨ Features

### 📖 Book Management
- **CRUD Operations**: Create, read, update, and delete books
- **Search & Filter**: Search books by title and filter by category
- **Rich Details**: View comprehensive book information including authors and borrowing history
- **Modern UI**: Beautiful card-based layout with responsive design

### 👥 Author Management
- **Author Database**: Manage author information with biographies and birth years
- **Book-Author Relationships**: Link multiple authors to books
- **Author Profiles**: Detailed author pages with their published works

### 📋 Borrowing System
- **Loan Tracking**: Track book borrowings with borrower names and dates
- **Return Management**: Mark books as returned with automatic date tracking
- **Borrowing History**: View complete borrowing history for each book
- **Status Indicators**: Clear visual indicators for active and returned loans

### 📊 Statistics Dashboard
- **Library Overview**: Total books, authors, categories, and active borrowings
- **Category Distribution**: Visual breakdown of books by category
- **Popular Books**: Most borrowed books ranking
- **Quick Actions**: Easy access to common tasks

### 🔐 Authentication & Security
- **User Registration & Login**: Secure user authentication system
- **Role-Based Access**: Admin and regular user roles
- **Password Security**: Secure password hashing with Werkzeug
- **Session Management**: Flask-Login integration for secure sessions
- **Admin Dashboard**: Comprehensive admin panel with user management

### 🎨 Modern Design
- **Tailwind CSS**: Modern, responsive design with CDN integration
- **Font Awesome Icons**: Beautiful icons throughout the interface
- **Interactive Elements**: Hover effects, transitions, and smooth animations
- **Mobile Responsive**: Works perfectly on all device sizes

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- PostgreSQL (optional, defaults to SQLite)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Hackaton-Project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (optional)
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://username:password@localhost/library_db
   FLASK_SECRET_KEY=your-secret-key-here
   FLASK_ENV=development
   ```

4. **Run the application**
   ```bash
   python index.py
   ```

5. **Access the application**
   Open your browser and go to `http://localhost:5000`

6. **Login with default accounts**
   - **Admin**: `admin` / `admin123` (full access)
   - **User**: `user` / `user123` (standard access)

## 🗄️ Database Schema

### Tables
- **users**: User accounts (username, email, password, admin status)
- **books**: Book information (title, description, publication year, category)
- **authors**: Author information (name, biography, birth year)
- **categories**: Book categories (name, description)
- **books_authors**: Many-to-many relationship between books and authors
- **borrowings**: Borrowing records (book, borrower, dates)

### Sample Data
The system comes with pre-loaded sample data including:
- 2 default user accounts (admin and regular user)
- 5 book categories (Fiction, Science, History, Biography, Fantasy)
- 10 famous authors (J.K. Rowling, George Orwell, etc.)
- 10 classic books with proper author relationships

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Authentication**: Flask-Login with secure password hashing
- **Database**: SQLAlchemy ORM with PostgreSQL/SQLite
- **Frontend**: HTML5, Tailwind CSS (CDN), Font Awesome Icons
- **Package Management**: uv (Python package manager)

## 📁 Project Structure

```
Hackaton-Project/
├── database/           # Database configuration and seed data
│   ├── index.py       # Database initialization
│   └── seed/          # SQL seed data
├── models/            # SQLAlchemy models
│   └── library_models.py
├── templates/         # Jinja2 HTML templates
│   ├── base.html      # Base template with navigation
│   ├── index.html     # Books listing with search/filter
│   ├── create.html    # Add new book form
│   ├── edit.html      # Edit book form
│   ├── details.html   # Book details page
│   ├── authors.html   # Authors listing
│   ├── create_author.html # Add new author form
│   ├── author_details.html # Author details page
│   ├── borrowings.html # Borrowings management
│   ├── borrow_book.html # Borrow book form
│   └── stats.html     # Statistics dashboard
├── static/           # Static files (CSS, JS, images)
├── index.py          # Main Flask application
├── main.py           # Entry point
├── requirements.txt  # Python dependencies
└── pyproject.toml    # Project configuration
```

## 🎯 Key Features Explained

### Search & Filter System
- **Real-time Search**: Search books by title with instant results
- **Category Filtering**: Filter books by category with dropdown selection
- **Combined Filters**: Use search and category filters together
- **Clear Filters**: Easy reset to view all books

### Responsive Design
- **Mobile-First**: Designed to work perfectly on mobile devices
- **Grid Layout**: Responsive grid that adapts to screen size
- **Touch-Friendly**: Large buttons and touch targets for mobile users
- **Modern UI**: Clean, professional design with consistent spacing

### Data Validation
- **Form Validation**: Client-side and server-side validation
- **Error Handling**: User-friendly error messages with flash notifications
- **Data Integrity**: Proper foreign key relationships and constraints
- **Input Sanitization**: Protection against common input issues

## 🔧 Configuration

### Environment Variables
- `DATABASE_URL`: Database connection string (defaults to SQLite)
- `FLASK_SECRET_KEY`: Secret key for session management
- `FLASK_ENV`: Environment mode (development/production)

### Database Options
- **SQLite**: Default, no setup required
- **PostgreSQL**: For production use, requires PostgreSQL server

## 📈 Future Enhancements

- [ ] User authentication and authorization
- [ ] Advanced search with multiple criteria
- [ ] Book cover image upload
- [ ] Email notifications for overdue books
- [ ] Barcode scanning support
- [ ] Export/import functionality
- [ ] Advanced reporting and analytics
- [ ] Multi-language support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Acknowledgments

- Built with ❤️ using Flask and Tailwind CSS
- Icons provided by Font Awesome
- Sample data includes classic literature and famous authors
- Designed with modern web development best practices

---

**Happy Reading! 📚✨**
