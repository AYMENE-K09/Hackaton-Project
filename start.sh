#!/bin/bash

# Library Management System - Start Script
# This script activates the virtual environment and starts the Flask application

echo "============================================================"
echo "📚 Library Management System - Starting..."
echo "============================================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Installing dependencies..."
    ./venv/bin/pip install -r requirements.txt
fi

# Activate virtual environment and start the application
echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "🚀 Starting Flask application..."
echo "📱 Open your browser and go to: http://localhost:5000"
echo "⏹️  Press Ctrl+C to stop the server"
echo "============================================================"

# Start the Flask application
python run.py
