# 🚀 Quick Start Guide

## Installation & Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python run.py
```
Or alternatively:
```bash
python index.py
```

### 3. Access the Application
Open your browser and go to: **http://localhost:5000**

## 🎯 What You Can Do

### 📚 Books Management
- **View Books**: Browse all books in a beautiful card layout
- **Search**: Search books by title
- **Filter**: Filter books by category
- **Add Book**: Create new books with authors and categories
- **Edit Book**: Update book information
- **Delete Book**: Remove books from the library

### 👥 Authors Management
- **View Authors**: Browse all authors
- **Add Author**: Create new author profiles
- **Author Details**: View author information and their books

### 📋 Borrowing System
- **Borrow Books**: Track book loans
- **Return Books**: Mark books as returned
- **View History**: See complete borrowing history

### 📊 Statistics
- **Dashboard**: View library statistics
- **Category Breakdown**: See books by category
- **Popular Books**: Most borrowed books ranking

## 🎨 Features

- ✅ **Modern UI**: Beautiful design with Tailwind CSS
- ✅ **Responsive**: Works on desktop, tablet, and mobile
- ✅ **Search & Filter**: Find books quickly
- ✅ **Data Validation**: Proper form validation
- ✅ **Error Handling**: User-friendly error messages
- ✅ **Sample Data**: Pre-loaded with classic books and authors

## 🔧 Configuration

### Environment Variables (Optional)
Create a `.env` file for custom settings:
```env
DATABASE_URL=postgresql://username:password@localhost/library_db
FLASK_SECRET_KEY=your-secret-key-here
FLASK_ENV=development
```

### Database Options
- **SQLite** (default): No setup required
- **PostgreSQL**: For production use

## 📱 Mobile Support
The application is fully responsive and works great on:
- 📱 Mobile phones
- 📱 Tablets
- 💻 Desktop computers

## 🆘 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Kill process using port 5000
   lsof -ti:5000 | xargs kill -9
   ```

2. **Missing dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database issues**
   ```bash
   # Delete existing database to start fresh
   rm library.db
   python run.py
   ```

## 🎉 Enjoy Your Library!

The system comes with sample data including:
- 5 book categories
- 10 famous authors
- 10 classic books

Start by exploring the books, adding new ones, or checking out the statistics dashboard!

---

**Need help?** Check the full README.md for detailed documentation.
