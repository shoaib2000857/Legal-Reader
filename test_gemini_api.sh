#!/bin/bash

# Gemini API Health Check Script
# This script tests the Gemini API connectivity and response status

echo "🔍 Testing Gemini API Connectivity..."
echo "=====================================\n"

# Check if API key is provided
if [ -z "$1" ]; then
    echo "❌ Error: API key required"
    echo "Usage: $0 <YOUR_GOOGLE_API_KEY>"
    echo ""
    echo "Example:"
    echo "  $0 AIzaSyD0ZXHG_KDTWOn9rn5XkVpFvOkt83yRLXE"
    echo ""
    echo "Get your API key from: https://makersuite.google.com/app/apikey"
    exit 1
fi

API_KEY="$1"

echo "📡 Testing API endpoint..."

# Basic curl command to test Gemini API
curl -X POST \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $API_KEY" \
  -d '{
    "contents": [{
      "parts": [{
        "text": "Hello, can you respond with just the word SUCCESS if you receive this message?"
      }]
    }]
  }' \
  -w "\n\n📊 Response Status: %{http_code}\n📏 Response Size: %{size_download} bytes\n⏱️  Response Time: %{time_total} seconds\n" \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

echo "\n🔍 Testing with verbose output..."
echo "================================\n"

# More detailed curl with verbose output
curl -v -X POST \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $API_KEY" \
  -d '{
    "contents": [{
      "parts": [{
        "text": "Test message"
      }]
    }]
  }' \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent" \
  2>&1 | head -20

echo "\n✅ API test completed!"
