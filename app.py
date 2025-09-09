"""
Legal Document Analyzer - Main Streamlit Application
AI-powered tool to simplify complex legal documents
"""
import streamlit as st
import os
import sys
from pathlib import Path
import pandas as pd
from datetime import datetime

# Add src directory to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

from src.utils.document_processor import DocumentProcessor
from src.utils.ai_analyzer import LegalDocumentAnalyzer
from src.components.ui_components import (
    render_document_upload, render_document_info, render_analysis_tabs,
    render_chat_interface, render_document_stats, render_sidebar,
    render_loading_spinner, render_error_message, render_success_message,
    render_info_message
)


def main():
    """Main application function"""
    # Page configuration
    st.set_page_config(
        page_title="Legal Reader - AI Document Analyzer",
        page_icon="⚖️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        padding: 8px;
        border-radius: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #4a4a4a !important;
        color: #ffffff !important;
        border: 2px solid #666666 !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #5a5a5a !important;
        border-color: #2196f3 !important;
        color: #ffffff !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2196f3 !important;
        color: white !important;
        border-color: #1976d2 !important;
        box-shadow: 0 2px 8px rgba(33, 150, 243, 0.3) !important;
    }
    /* Keep content area with default theme colors */
    .stTabs [data-baseweb="tab-panel"] {
        border-radius: 0 0 12px 12px;
        padding: 24px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>⚖️ Legal Reader</h1>
        <p>AI-Powered Legal Document Analyzer</p>
        <p><em>Simplifying complex legal documents into clear, accessible guidance</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Render sidebar
    render_sidebar()
    
    # Initialize session state
    if 'document_processed' not in st.session_state:
        st.session_state.document_processed = False
    if 'analysis_complete' not in st.session_state:
        st.session_state.analysis_complete = False
    
    # Check for API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        st.error("""
        🔑 **Google API Key Required**
        
        To use this application, you need to set up a Google API key:
        1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
        2. Create a new API key
        3. Set the environment variable: `GOOGLE_API_KEY=your_api_key_here`
        4. Or create a `.env` file with your API key
        """)
        st.stop()
    
    try:
        # Initialize processors
        doc_processor = DocumentProcessor()
        ai_analyzer = LegalDocumentAnalyzer(api_key)
        
        # Step 1: Document Upload
        uploaded_file = render_document_upload()
        
        if uploaded_file is not None:
            try:
                # Process the uploaded document
                with render_loading_spinner("Processing document..."):
                    file_content = uploaded_file.read()
                    doc_info = doc_processor.process_document(file_content, uploaded_file.name)
                    st.session_state.doc_info = doc_info
                    st.session_state.document_processed = True
                
                render_success_message("Document processed successfully!")
                
                # Display document information
                render_document_info(doc_info)
                render_document_stats(doc_info)
                
                # Step 2: AI Analysis
                if st.session_state.document_processed:
                    st.markdown("---")
                    
                    # Show document type detection
                    with st.container():
                        col1, col2 = st.columns([2, 1])
                        with col1:
                            if st.button("🚀 Start AI Analysis", type="primary", use_container_width=True):
                                with render_loading_spinner("Analyzing document with AI... This may take a moment."):
                                    try:
                                        # Get document type
                                        doc_type = ai_analyzer.get_document_type(doc_info['text'])
                                        
                                        # Perform comprehensive analysis
                                        analysis_results = ai_analyzer.comprehensive_analysis(doc_info['text'])
                                        
                                        st.session_state.analysis_results = analysis_results
                                        st.session_state.doc_type = doc_type
                                        st.session_state.analysis_complete = True
                                        
                                        render_success_message("Analysis completed!")
                                        
                                    except Exception as e:
                                        render_error_message(f"Analysis failed: {str(e)}")
                        
                        with col2:
                            if st.session_state.get('doc_type'):
                                st.info(f"📄 **Document Type**: {st.session_state.doc_type}")
                
                # Step 3: Display Analysis Results
                if st.session_state.analysis_complete:
                    st.markdown("---")
                    render_analysis_tabs(st.session_state.analysis_results)
                    
                    # Step 4: Q&A Chat Interface
                    st.markdown("---")
                    render_chat_interface(doc_info['text'], ai_analyzer)
                    
                    # Download analysis report
                    st.markdown("---")
                    st.subheader("📄 Download Analysis Report")
                    
                    # Create a text report
                    report = f"""
LEGAL DOCUMENT ANALYSIS REPORT
==============================

Document: {doc_info['file_name']}
Type: {st.session_state.get('doc_type', 'Unknown')}
Word Count: {doc_info['word_count']:,}
Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

SUMMARY
-------
{st.session_state.analysis_results.get('summary', 'Not available')}

KEY TERMS & CLAUSES
-------------------
{st.session_state.analysis_results.get('key_terms', 'Not available')}

RISKS & RED FLAGS
-----------------
{st.session_state.analysis_results.get('risks', 'Not available')}

PLAIN ENGLISH EXPLANATION
--------------------------
{st.session_state.analysis_results.get('plain_english', 'Not available')}

RECOMMENDED ACTIONS
-------------------
{st.session_state.analysis_results.get('action_items', 'Not available')}

DISCLAIMER
----------
This analysis is provided for informational purposes only and should not replace 
professional legal advice. Always consult with a qualified attorney for important legal matters.
                    """
                    
                    st.download_button(
                        label="📥 Download Analysis Report",
                        data=report,
                        file_name=f"legal_analysis_{doc_info['file_name'].split('.')[0]}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
            
            except Exception as e:
                render_error_message(f"Error processing document: {str(e)}")
        
        else:
            # Show information about the app when no document is uploaded
            st.markdown("---")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🎯 What We Do")
                st.write("""
                Legal Reader uses advanced AI to analyze legal documents and provide:
                
                - **📋 Clear Summaries**: Understand what the document is about
                - **🔑 Key Terms**: Important clauses explained in simple language
                - **⚠️ Risk Analysis**: Potential red flags and unfavorable terms
                - **💬 Plain English**: Complex legal language simplified
                - **✅ Action Items**: What you should do before signing
                - **💬 Q&A Chat**: Ask specific questions about your document
                """)
            
            with col2:
                st.subheader("📁 Supported Documents")
                st.write("""
                Upload any of these legal document types:
                
                - **Rental/Lease Agreements**
                - **Employment Contracts**
                - **Loan Agreements**
                - **Terms of Service**
                - **Privacy Policies**
                - **Purchase Agreements**
                - **Service Contracts**
                - **NDAs & Confidentiality Agreements**
                
                *Supported formats: PDF, DOCX, TXT*
                """)
            
            st.markdown("---")
            st.info("""
            🚀 **Get Started**: Upload a legal document above to begin your AI-powered analysis!
            """)
    
    except Exception as e:
        render_error_message(f"Application error: {str(e)}")
        st.write("Please check your API key and try refreshing the page.")


if __name__ == "__main__":
    main()
