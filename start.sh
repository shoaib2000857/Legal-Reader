#!/bin/bash

# Legal Document Analyzer - Start Script
echo "🏛️ Starting Legal Document Analyzer..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️ .env file not found!"
    echo "Please create a .env file with your Google API key:"
    echo "GOOGLE_API_KEY=AIzaSyD0ZXHG_KDTWOn9rn5XkVpFvOkt83yRLXE"
    echo ""
    echo "Get your API key from: https://makersuite.google.com/app/apikey"
    exit 1
fi

# Check if Google API key is set
if ! grep -q "GOOGLE_API_KEY=" .env || grep -q "your_google_api_key_here" .env; then
    echo "⚠️ Google API key not configured!"
    echo "Please edit the .env file and add your Google API key:"
    echo "GOOGLE_API_KEY=your_actual_api_key"
    exit 1
fi

echo "✅ Configuration looks good!"
echo "🚀 Starting Streamlit application..."

# Start the Streamlit app
streamlit run app.py
