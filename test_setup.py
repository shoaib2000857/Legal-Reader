"""
Test script for Legal Document Analyzer
"""
import sys
import os
from pathlib import Path

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Streamlit: {e}")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ Google Generative AI imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Google Generative AI: {e}")
        return False
    
    try:
        import PyPDF2
        print("✅ PyPDF2 imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import PyPDF2: {e}")
        return False
    
    try:
        import docx
        print("✅ python-docx imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import python-docx: {e}")
        return False
    
    try:
        import plotly
        print("✅ Plotly imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Plotly: {e}")
        return False
    
    return True

def test_env_file():
    """Test if .env file exists"""
    print("\nTesting environment configuration...")
    
    if os.path.exists('.env'):
        print("✅ .env file found")
        
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('GOOGLE_API_KEY')
        if api_key and api_key != 'your_google_api_key_here':
            print("✅ Google API key configured")
            return True
        else:
            print("⚠️ Google API key not configured in .env file")
            return False
    else:
        print("❌ .env file not found")
        return False

def test_project_structure():
    """Test if project structure is correct"""
    print("\nTesting project structure...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'src/utils/document_processor.py',
        'src/utils/ai_analyzer.py',
        'src/components/ui_components.py'
    ]
    
    required_dirs = [
        'src',
        'src/utils',
        'src/components',
        'data',
        'data/sample_documents'
    ]
    
    all_good = True
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} found")
        else:
            print(f"❌ {file_path} missing")
            all_good = False
    
    for dir_path in required_dirs:
        if os.path.isdir(dir_path):
            print(f"✅ {dir_path}/ directory found")
        else:
            print(f"❌ {dir_path}/ directory missing")
            all_good = False
    
    return all_good

def main():
    """Run all tests"""
    print("🧪 Legal Document Analyzer - Test Suite")
    print("=" * 50)
    
    tests_passed = 0
    total_tests = 3
    
    if test_imports():
        tests_passed += 1
    
    if test_env_file():
        tests_passed += 1
    
    if test_project_structure():
        tests_passed += 1
    
    print("\n" + "=" * 50)
    print(f"Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nTo run the application:")
        print("streamlit run app.py")
    else:
        print("⚠️ Some tests failed. Please check the setup.")
        
        if tests_passed < 1:
            print("\n📦 Try running: pip install -r requirements.txt")
        
        if not os.path.exists('.env'):
            print("\n🔑 Create .env file and add your Google API key")
    
    return tests_passed == total_tests

if __name__ == "__main__":
    main()
