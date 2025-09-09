#!/bin/bash

# Enhanced Gemini API Test Script with Various Prompts
# This script tests different types of questions and prompts

echo "🧪 Enhanced Gemini API Testing Suite"
echo "====================================="

# Check if API key is provided
if [ -z "$1" ]; then
    echo "❌ Error: API key required"
    echo "Usage: $0 <YOUR_GOOGLE_API_KEY>"
    exit 1
fi

API_KEY="$1"
BASE_URL="https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

# Function to test a prompt
test_prompt() {
    local test_name="$1"
    local prompt="$2"
    
    echo "🔍 Testing: $test_name"
    echo "Prompt: $prompt"
    echo "----------------------------------------"
    
    response=$(curl -s -X POST \
        -H "Content-Type: application/json" \
        -H "x-goog-api-key: $API_KEY" \
        -d "{
            \"contents\": [{
                \"parts\": [{
                    \"text\": \"$prompt\"
                }]
            }]
        }" \
        "$BASE_URL")
    
    # Extract just the text response
    echo "$response" | grep -o '"text": *"[^"]*"' | sed 's/"text": *"\(.*\)"/\1/' | head -1
    
    # Check status
    if echo "$response" | grep -q '"text"'; then
        echo "✅ Status: SUCCESS"
    else
        echo "❌ Status: FAILED"
        echo "Raw response: $response"
    fi
    
    echo ""
    echo "════════════════════════════════════════"
    echo ""
}

# Test 1: Simple greeting
test_prompt "Simple Greeting" "Hello! Can you introduce yourself?"

# Test 2: Legal document analysis capability
test_prompt "Legal Analysis Capability" "Can you analyze legal documents and explain complex terms in simple language?"

# Test 3: Document type identification
test_prompt "Document Type Recognition" "If I give you a text that says 'RENTAL AGREEMENT between landlord and tenant for property located at...', what type of document is this?"

# Test 4: Risk identification
test_prompt "Risk Assessment" "What are common red flags someone should look for in a rental agreement before signing?"

# Test 5: Plain English explanation
test_prompt "Plain English Translation" "How would you explain the legal term 'indemnification clause' to a regular person?"

# Test 6: Practical advice
test_prompt "Practical Guidance" "What should someone do before signing any legal contract?"

# Test 7: Specific legal scenario
test_prompt "Legal Scenario Analysis" "If a contract says 'Tenant is responsible for all repairs regardless of cause', is this fair? What should the tenant do?"

# Test 8: Technical capability test
test_prompt "Technical Analysis" "Can you extract key information from documents and format it as structured summaries?"

# Test 9: Complex reasoning
test_prompt "Complex Legal Reasoning" "Explain the difference between 'normal wear and tear' and 'damage' in a rental context with examples."

# Test 10: Action-oriented advice
test_prompt "Actionable Recommendations" "Give me a 5-step checklist for reviewing any legal document before signing."

echo "🎯 All tests completed!"
echo ""
echo "💡 Usage Examples for Your Legal Reader App:"
echo "• Document Summary: 'Summarize this lease agreement in simple terms'"
echo "• Risk Analysis: 'What potential risks should I be aware of in this contract?'"
echo "• Key Terms: 'Explain the most important clauses in this document'"
echo "• Plain English: 'Rewrite this legal section in everyday language'"
echo "• Action Items: 'What should I do before signing this agreement?'"
