#!/bin/bash

# Real Legal Document Testing Script
# Tests Gemini API with actual legal text snippets

echo "📋 Legal Document Analysis Testing"
echo "=================================="

if [ -z "$1" ]; then
    echo "❌ Error: API key required"
    echo "Usage: $0 <YOUR_GOOGLE_API_KEY>"
    exit 1
fi

API_KEY="$1"
BASE_URL="https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

# Function to test legal analysis
test_legal_analysis() {
    local test_name="$1"
    local document_text="$2"
    local question="$3"
    
    echo "🔍 Test: $test_name"
    echo "Question: $question"
    echo "----------------------------------------"
    
    # Escape quotes in the document text
    escaped_text=$(echo "$document_text" | sed 's/"/\\"/g')
    escaped_question=$(echo "$question" | sed 's/"/\\"/g')
    
    prompt="Document text: $escaped_text\n\nQuestion: $escaped_question"
    
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
    
    # Extract and display response
    echo "$response" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    if 'candidates' in data and len(data['candidates']) > 0:
        text = data['candidates'][0]['content']['parts'][0]['text']
        print('📝 Response:')
        print(text)
        print('✅ Status: SUCCESS')
    else:
        print('❌ Status: FAILED - No response text')
        print('Raw:', data)
except:
    print('❌ Status: ERROR - Invalid JSON response')
" 2>/dev/null || echo "❌ Python parsing failed"
    
    echo ""
    echo "════════════════════════════════════════"
    echo ""
}

# Sample legal texts for testing

# Test 1: Lease Agreement Clause
LEASE_TEXT="LATE PAYMENT: If rent is not received by the 5th day of the month, Tenant shall pay a late fee of \$50.00. If rent remains unpaid for more than 10 days after the due date, Landlord may begin eviction proceedings and Tenant shall be responsible for all legal costs and attorney fees."

test_legal_analysis "Lease Late Fee Analysis" "$LEASE_TEXT" "What does this clause mean and what should a tenant be concerned about?"

# Test 2: Employment Contract Clause
EMPLOYMENT_TEXT="Employee agrees that during employment and for a period of two (2) years after termination, Employee shall not directly or indirectly compete with Company within a fifty (50) mile radius of any Company location."

test_legal_analysis "Non-Compete Clause Analysis" "$EMPLOYMENT_TEXT" "Is this non-compete clause reasonable? What are the potential risks for the employee?"

# Test 3: Loan Agreement Terms
LOAN_TEXT="In the event of default, the entire unpaid principal balance, together with accrued interest and fees, shall become immediately due and payable. Borrower waives any right to notice of acceleration and agrees to pay all collection costs including reasonable attorney fees."

test_legal_analysis "Loan Default Terms" "$LOAN_TEXT" "Explain what happens if someone defaults on this loan and what 'acceleration' means."

# Test 4: Terms of Service
TOS_TEXT="Company may modify these Terms at any time by posting the revised Terms on the website. Your continued use of the Service after such posting constitutes acceptance of the modified Terms."

test_legal_analysis "Terms Modification Clause" "$TOS_TEXT" "What does this mean for users? How can they protect themselves?"

# Test 5: Indemnification Clause
INDEMNITY_TEXT="Client agrees to indemnify, defend, and hold harmless Company from and against any and all claims, damages, losses, costs, and expenses (including reasonable attorney fees) arising from Client's use of the services."

test_legal_analysis "Indemnification Analysis" "$INDEMNITY_TEXT" "Explain this indemnification clause in simple terms. What is the client agreeing to?"

echo "🎯 Legal Document Testing Complete!"
echo ""
echo "💡 These tests demonstrate the AI's ability to:"
echo "• Analyze complex legal language"
echo "• Identify potential risks and concerns"
echo "• Explain legal concepts in plain English"
echo "• Provide practical advice and warnings"
echo "• Break down technical legal terms"
