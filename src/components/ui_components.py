"""
Streamlit components for the Legal Document Analyzer
"""
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, Any


def render_document_upload() -> Any:
    """Render document upload component"""
    st.header("📄 Upload Legal Document")
    st.write("Upload your legal document for AI-powered analysis. Supported formats: PDF, DOCX, TXT")
    
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=['pdf', 'docx', 'txt'],
        help="Upload a legal document to get started with the analysis"
    )
    
    return uploaded_file


def render_document_info(doc_info: Dict[str, Any]):
    """Render document information"""
    st.subheader("📊 Document Information")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("File Name", doc_info['file_name'])
    
    with col2:
        st.metric("Word Count", f"{doc_info['word_count']:,}")
    
    with col3:
        st.metric("File Type", doc_info['file_type'].upper())
    
    # Show document preview
    with st.expander("📖 Document Preview"):
        preview_text = doc_info['text'][:1000] + "..." if len(doc_info['text']) > 1000 else doc_info['text']
        st.text_area("First 1000 characters:", preview_text, height=200, disabled=True)


def render_analysis_tabs(analysis_results: Dict[str, str]):
    """Render analysis results in tabs"""
    st.header("🔍 AI Analysis Results")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Summary", 
        "🔑 Key Terms", 
        "⚠️ Risks & Red Flags", 
        "💬 Plain English", 
        "✅ Action Items"
    ])
    
    with tab1:
        st.subheader("Document Summary")
        st.write(analysis_results.get('summary', 'Analysis not available'))
    
    with tab2:
        st.subheader("Key Terms & Clauses")
        st.write(analysis_results.get('key_terms', 'Analysis not available'))
    
    with tab3:
        st.subheader("Potential Risks & Red Flags")
        st.warning("⚠️ Please review these potential concerns carefully:")
        st.write(analysis_results.get('risks', 'Analysis not available'))
    
    with tab4:
        st.subheader("Plain English Translation")
        st.info("📝 Here's the document explained in simple terms:")
        st.write(analysis_results.get('plain_english', 'Analysis not available'))
    
    with tab5:
        st.subheader("Recommended Actions")
        st.success("✅ Here's what you should do before signing:")
        st.write(analysis_results.get('action_items', 'Analysis not available'))


def render_chat_interface(document_text: str, ai_analyzer):
    """Render chat interface for Q&A"""
    st.header("💬 Ask Questions About Your Document")
    st.write("Have specific questions about your document? Ask our AI assistant!")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask a question about your document..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = ai_analyzer.answer_question(document_text, prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_msg = f"Sorry, I encountered an error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})


def render_document_stats(doc_info: Dict[str, Any]):
    """Render document statistics visualization"""
    st.subheader("📈 Document Statistics")
    
    # Create metrics
    col1, col2 = st.columns(2)
    
    with col1:
        # Word count visualization
        fig_words = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = doc_info['word_count'],
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Word Count"},
            gauge = {
                'axis': {'range': [None, max(5000, doc_info['word_count'])]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 1000], 'color': "lightgray"},
                    {'range': [1000, 3000], 'color': "gray"},
                    {'range': [3000, 5000], 'color': "lightblue"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': doc_info['word_count']
                }
            }
        ))
        fig_words.update_layout(height=300)
        st.plotly_chart(fig_words, use_container_width=True)
    
    with col2:
        # Character count visualization
        fig_chars = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = doc_info['character_count'],
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Character Count"},
            gauge = {
                'axis': {'range': [None, max(25000, doc_info['character_count'])]},
                'bar': {'color': "darkgreen"},
                'steps': [
                    {'range': [0, 5000], 'color': "lightgray"},
                    {'range': [5000, 15000], 'color': "gray"},
                    {'range': [15000, 25000], 'color': "lightgreen"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': doc_info['character_count']
                }
            }
        ))
        fig_chars.update_layout(height=300)
        st.plotly_chart(fig_chars, use_container_width=True)


def render_sidebar():
    """Render sidebar with app information"""
    with st.sidebar:
        st.title("🏛️ Legal Reader")
        st.markdown("---")
        
        st.subheader("📚 About")
        st.write("""
        Legal Reader is an AI-powered tool that helps you understand complex legal documents 
        by providing clear summaries, identifying risks, and answering your questions in plain English.
        """)
        
        st.markdown("---")
        
        st.subheader("🚀 Features")
        st.write("""
        - **Document Analysis**: Get comprehensive summaries
        - **Risk Detection**: Identify potential red flags
        - **Plain English**: Complex terms simplified
        - **Q&A Chat**: Ask questions about your document
        - **Action Items**: Know what to do before signing
        """)
        
        st.markdown("---")
        
        st.subheader("⚖️ Disclaimer")
        st.warning("""
        This tool provides general information and should not replace professional legal advice. 
        Always consult with a qualified attorney for important legal matters.
        """)
        
        st.markdown("---")
        
        st.subheader("🔒 Privacy")
        st.info("""
        Your documents are processed securely and are not stored or shared. 
        Each session is independent and private.
        """)


def render_loading_spinner(message: str = "Analyzing document..."):
    """Render loading spinner with message"""
    return st.spinner(message)


def render_error_message(error: str):
    """Render error message"""
    st.error(f"❌ Error: {error}")


def render_success_message(message: str):
    """Render success message"""
    st.success(f"✅ {message}")


def render_info_message(message: str):
    """Render info message"""
    st.info(f"ℹ️ {message}")
