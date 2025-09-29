#!/usr/bin/env python3
"""
Library Management System - Quick Start Script
Run this file to start the application with default settings.
"""

import os
import sys
from datetime import datetime

def main():
    print("=" * 60)
    print("📚 Library Management System")
    print("=" * 60)
    print(f"Starting at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Check if virtual environment is activated
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Virtual environment not detected!")
        print("For best results, activate the virtual environment first:")
        print("source venv/bin/activate")
        print()
    
    # Set default environment variables if not set
    if not os.environ.get('FLASK_SECRET_KEY'):
        os.environ['FLASK_SECRET_KEY'] = 'dev-secret-key-change-in-production'
        print("🔑 Using default Flask secret key (change in production)")
    
    if not os.environ.get('DATABASE_URL'):
        os.environ['DATABASE_URL'] = 'sqlite:///library.db'
        print("🗄️  Using SQLite database (library.db)")
    
    print("🌐 Starting Flask development server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 60)
    print()
    
    # Import and run the Flask app
    try:
        from index import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except ImportError as e:
        print(f"❌ Error importing Flask app: {e}")
        print("Make sure you have installed all dependencies:")
        print("pip install -r requirements.txt")
        print("Or activate virtual environment and run:")
        print("source venv/bin/activate")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
