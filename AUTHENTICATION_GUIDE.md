# 🔐 Authentication & Admin Guide

## 🚀 Quick Start with Authentication

### Default Accounts
The system comes with pre-created accounts for testing:

**Admin Account:**
- Username: `admin`
- Password: `admin123`
- Access: Full admin privileges

**Regular User Account:**
- Username: `user`
- Password: `user123`
- Access: Standard user privileges

## 🔑 Authentication Features

### User Registration
- **Public Registration**: Anyone can create an account
- **Email Validation**: Valid email addresses required
- **Password Security**: Minimum 6 characters
- **Username Uniqueness**: Each username must be unique

### Login System
- **Secure Authentication**: Password hashing with Werkzeug
- **Session Management**: Flask-Login integration
- **Remember Me**: Optional persistent login
- **Redirect After Login**: Returns to intended page

### User Roles
- **Regular Users**: Can view books, borrow books, view statistics
- **Admin Users**: Full access including user management and admin dashboard

## 🛡️ Access Control

### Protected Routes
The following routes require authentication:
- `/create` - Add new books
- `/edit/<id>` - Edit books
- `/delete/<id>` - Delete books
- `/authors/create` - Add new authors
- `/borrow/<id>` - Borrow books
- `/return/<id>` - Return books

### Admin-Only Routes
The following routes require admin privileges:
- `/admin` - Admin dashboard
- `/admin/users` - User management
- `/admin/toggle-admin/<id>` - Change user privileges

## 👨‍💼 Admin Dashboard Features

### Overview Statistics
- Total books, authors, categories, users
- Active borrowings vs total borrowings
- Recent activity monitoring

### User Management
- View all registered users
- See user roles (Admin/User)
- Grant/revoke admin privileges
- View registration dates

### Recent Activity
- Latest books added
- New user registrations
- Recent borrowing activity

### Quick Actions
- Direct links to add books/authors
- User management access
- Borrowing management

## 🔧 User Management

### Creating New Users
1. Users can register themselves via `/register`
2. Admins can view all users in `/admin/users`
3. System automatically assigns regular user role

### Admin Privileges
- **Grant Admin**: Click the user-plus icon next to any user
- **Revoke Admin**: Click the user-minus icon next to admin users
- **Self-Protection**: Admins cannot modify their own privileges

### User Information
- Username and email display
- Registration date and time
- Current role (Admin/User)
- User ID for reference

## 🎨 UI/UX Features

### Navigation Updates
- **Logged Out**: Shows Login and Register buttons
- **Logged In**: Shows welcome message and logout button
- **Admin Users**: Additional Admin dashboard link
- **Protected Actions**: Hidden for non-authenticated users

### Visual Indicators
- **Admin Badge**: Red crown icon for admin users
- **User Badge**: Green user icon for regular users
- **Role Colors**: Consistent color coding throughout

### Responsive Design
- Mobile-friendly login/register forms
- Responsive admin dashboard
- Touch-friendly user management interface

## 🔒 Security Features

### Password Security
- **Hashing**: Passwords stored as secure hashes
- **No Plain Text**: Never store passwords in plain text
- **Werkzeug Security**: Industry-standard password hashing

### Session Security
- **Secure Sessions**: Flask-Login session management
- **CSRF Protection**: Built-in CSRF protection
- **Session Timeout**: Automatic session expiration

### Access Control
- **Route Protection**: Decorators prevent unauthorized access
- **Role-Based Access**: Admin-only features properly protected
- **User Isolation**: Users cannot access other users' data

## 📱 Mobile Support

### Responsive Authentication
- Mobile-optimized login/register forms
- Touch-friendly buttons and inputs
- Responsive admin dashboard
- Mobile navigation with authentication status

## 🚀 Getting Started

### 1. Start the Application
```bash
python run.py
```

### 2. Access the System
- Open browser to `http://localhost:5000`
- Click "Login" in the navigation
- Use default admin account: `admin` / `admin123`

### 3. Explore Admin Features
- Click "Admin" in navigation (admin users only)
- View comprehensive dashboard
- Manage users and their privileges
- Monitor system activity

### 4. Test User Features
- Logout and register a new account
- Test regular user functionality
- Try accessing admin features (should be blocked)

## 🎯 Best Practices

### For Administrators
- Change default admin password in production
- Regularly review user accounts
- Monitor system activity through dashboard
- Use strong passwords for admin accounts

### For Users
- Use strong, unique passwords
- Logout when finished
- Report any security concerns
- Keep account information updated

## 🔧 Configuration

### Environment Variables
```env
FLASK_SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url
```

### Security Settings
- Secret key for session security
- Database configuration
- Debug mode settings

## 🆘 Troubleshooting

### Common Issues

1. **Cannot Login**
   - Check username/password
   - Ensure account exists
   - Try default accounts first

2. **Admin Access Denied**
   - Verify user has admin privileges
   - Check if logged in as correct user
   - Contact system administrator

3. **Session Issues**
   - Clear browser cookies
   - Restart application
   - Check secret key configuration

### Support
- Check the main README.md for general setup
- Review error messages in browser console
- Check application logs for detailed errors

---

**🔐 Your library system now has enterprise-grade authentication and user management!**
