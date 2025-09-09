#!/bin/bash

# Legal Document Analyzer Setup Script
echo "🏛️ Setting up Legal Document Analyzer..."

# Create virtual environment
echo "Creating virtual environment..."
python -m venv legal_reader_env

# Activate virtual environment
echo "Activating virtual environment..."
source legal_reader_env/bin/activate

# Install requirements
echo "Installing Python packages..."
pip install -r requirements.txt

# Create .env file from example
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please edit .env file and add your Google API key!"
fi

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit the .env file and add your Google API key"
echo "2. Get your API key from: https://makersuite.google.com/app/apikey"
echo "3. Run the application with: streamlit run app.py"
echo ""
echo "To activate the environment in the future, run:"
echo "source legal_reader_env/bin/activate"
