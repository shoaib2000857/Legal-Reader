#!/bin/bash

# Test Gemini 2.5 Flash-Lite Model
echo "🧪 Testing Gemini 2.5 Flash-Lite Model"
echo "======================================"

if [ -z "$1" ]; then
    echo "❌ Error: API key required"
    echo "Usage: $0 <YOUR_GOOGLE_API_KEY>"
    exit 1
fi

API_KEY="$1"

# Test the new model
echo "📡 Testing gemini-2.5-flash-lite..."

curl -X POST \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $API_KEY" \
  -d '{
    "contents": [{
      "parts": [{
        "text": "Hello! Please respond with: SUCCESS - Gemini 2.5 Flash-Lite is working! This model has 1,000 requests per day."
      }]
    }]
  }' \
  -w "\n\n📊 Response Status: %{http_code}\n⏱️  Response Time: %{time_total} seconds\n" \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"

echo ""
echo "✅ If you see 'SUCCESS' above, the new model is working!"
echo ""
echo "🎯 Benefits of Gemini 2.5 Flash-Lite:"
echo "   • 1,000 requests per day (vs 50 with old model)"
echo "   • 15 requests per minute"
echo "   • 250,000 tokens per minute"
echo "   • Latest model with better performance"
