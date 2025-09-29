# 📦 Installation Guide

## Prerequisites
- Python 3.12 or higher
- pip (Python package installer)

## Installation Steps

### 1. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python run.py
```

## Alternative Installation Methods

### Using uv (Faster)
```bash
# Install uv if not already installed
pip install uv

# Install dependencies
uv pip install -r requirements.txt

# Run the application
python run.py
```

### Using pipx (Isolated)
```bash
# Install pipx if not already installed
pip install pipx

# Install dependencies in isolated environment
pipx install --include-deps -e .
```

## Troubleshooting

### Python Version Issues
Make sure you have Python 3.12 or higher:
```bash
python3 --version
```

### Permission Issues
If you get permission errors, use the virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Port Already in Use
If port 5000 is already in use:
```bash
# Kill process using port 5000
lsof -ti:5000 | xargs kill -9
```

### Database Issues
If you encounter database issues:
```bash
# Remove existing database
rm library.db

# Run the application (will create new database)
python run.py
```

## Verification

After installation, verify everything works:
```bash
python -c "from index import app; print('✅ Installation successful!')"
```

## Next Steps

1. Open your browser
2. Go to http://localhost:5000
3. Start using your library management system!

## Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Make sure all dependencies are installed
3. Verify Python version compatibility
4. Check the full README.md for detailed documentation
