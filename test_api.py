"""
Quick test script to verify Google Gemini API is working
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

def test_gemini_api():
    """Test basic Gemini API functionality"""
    print("🧪 Testing Google Gemini API...")
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key or api_key == 'your_google_api_key_here':
        print("❌ Please set your Google API key in .env file")
        return False
    
    try:
        # Configure Gemini
        genai.configure(api_key=api_key)
        
        # Test with gemini-1.5-flash (free model)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Simple test prompt
        test_prompt = "Explain what a legal contract is in one sentence."
        
        print("📤 Sending test prompt to Gemini...")
        response = model.generate_content(test_prompt)
        
        print("✅ API test successful!")
        print(f"📥 Response: {response.text}")
        return True
        
    except Exception as e:
        print(f"❌ API test failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_gemini_api()
    if success:
        print("\n🎉 Your setup is ready to use!")
    else:
        print("\n⚠️ Please fix the API configuration before proceeding.")
