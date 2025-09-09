"""
AI-powered legal document analyzer using Google Gemini
"""
import google.generativeai as genai
from typing import Dict, List, Any, Optional
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not available in cloud deployment
    pass
import json
import re


class LegalDocumentAnalyzer:
    """AI-powered analyzer for legal documents using Google Gemini"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("Google API key not found. Please set GOOGLE_API_KEY environment variable.")
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash-lite')  # Best balance: 1,000 RPD
        
        # Legal document analysis prompts
        self.prompts = {
            'summary': self._get_summary_prompt(),
            'key_terms': self._get_key_terms_prompt(),
            'risks': self._get_risks_prompt(),
            'plain_english': self._get_plain_english_prompt(),
            'action_items': self._get_action_items_prompt()
        }
    
    def _get_summary_prompt(self) -> str:
        return """
        You are a legal expert helping everyday people understand complex legal documents. 
        Please provide a concise, clear summary of this legal document in simple terms that anyone can understand.
        
        Focus on:
        - What type of document this is
        - The main purpose and key parties involved
        - Important dates and deadlines
        - Key obligations and rights
        
        Document text:
        {document_text}
        
        Provide your response in a structured format with clear headings.
        """
    
    def _get_key_terms_prompt(self) -> str:
        return """
        You are a legal expert. Analyze this legal document and identify the most important terms and clauses 
        that a regular person should understand. Explain each term in plain English.
        
        For each key term:
        - Quote the exact clause from the document
        - Explain what it means in simple terms
        - Explain why it's important
        
        Document text:
        {document_text}
        
        Format your response as a list of key terms with explanations.
        """
    
    def _get_risks_prompt(self) -> str:
        return """
        You are a legal expert helping people identify potential risks in legal documents.
        Analyze this document and identify potential risks, unfavorable terms, or red flags 
        that someone should be aware of before signing.
        
        For each risk:
        - Describe the potential risk clearly
        - Explain the possible consequences
        - Suggest what questions to ask or actions to take
        
        Document text:
        {document_text}
        
        Focus on practical risks that could affect the person financially or legally.
        """
    
    def _get_plain_english_prompt(self) -> str:
        return """
        You are a legal expert translator. Take this complex legal document and rewrite the most important 
        sections in plain, everyday English that a middle school student could understand.
        
        Focus on:
        - Main obligations of each party
        - Important rights and restrictions
        - Payment terms and penalties
        - Termination conditions
        
        Document text:
        {document_text}
        
        Rewrite the key sections clearly and concisely.
        """
    
    def _get_action_items_prompt(self) -> str:
        return """
        You are a legal advisor helping someone who needs to respond to this legal document.
        Based on this document, what specific actions should the person take before signing?
        
        Provide:
        - A checklist of things to do before signing
        - Questions to ask the other party
        - Documents or information to gather
        - Deadlines to be aware of
        - When to consult a lawyer
        
        Document text:
        {document_text}
        
        Make your recommendations practical and actionable.
        """
    
    def analyze_document(self, document_text: str, analysis_type: str = 'summary') -> str:
        """
        Analyze a legal document using AI
        
        Args:
            document_text: The extracted text from the legal document
            analysis_type: Type of analysis ('summary', 'key_terms', 'risks', 'plain_english', 'action_items')
            
        Returns:
            AI-generated analysis of the document
        """
        if analysis_type not in self.prompts:
            raise ValueError(f"Invalid analysis type: {analysis_type}")
        
        prompt = self.prompts[analysis_type].format(document_text=document_text)
        
        try:
            response = self.model.generate_content(prompt)
            if response.text:
                return response.text
            else:
                return f"Unable to generate {analysis_type} analysis. The response was empty."
        except Exception as e:
            error_msg = str(e)
            if "404" in error_msg or "not found" in error_msg.lower():
                return f"Model error: The AI model is currently unavailable. Please try again later."
            elif "quota" in error_msg.lower() or "limit" in error_msg.lower():
                return f"API limit reached: Please check your API quota or try again later."
            elif "api key" in error_msg.lower():
                return f"API key error: Please check your Google API key configuration."
            else:
                return f"Error generating {analysis_type} analysis: {error_msg}"
    
    def comprehensive_analysis(self, document_text: str) -> Dict[str, str]:
        """
        Perform a comprehensive analysis of the legal document
        
        Args:
            document_text: The extracted text from the legal document
            
        Returns:
            Dictionary with all types of analysis
        """
        results = {}
        
        for analysis_type in self.prompts.keys():
            try:
                results[analysis_type] = self.analyze_document(document_text, analysis_type)
            except Exception as e:
                results[analysis_type] = f"Unable to perform {analysis_type} analysis: {str(e)}"
        
        return results
    
    def answer_question(self, document_text: str, question: str) -> str:
        """
        Answer a specific question about the legal document
        
        Args:
            document_text: The extracted text from the legal document
            question: User's question about the document
            
        Returns:
            AI-generated answer to the question
        """
        prompt = f"""
        You are a legal expert helping someone understand a legal document. 
        Based on the document provided, please answer the following question in simple, clear terms.
        
        If the answer isn't clearly stated in the document, say so and provide general guidance.
        
        Document text:
        {document_text}
        
        Question: {question}
        
        Please provide a helpful, accurate answer in plain English.
        """
        
        try:
            response = self.model.generate_content(prompt)
            if response.text:
                return response.text
            else:
                return "I wasn't able to generate a response to your question. Please try rephrasing it."
        except Exception as e:
            error_msg = str(e)
            if "404" in error_msg or "not found" in error_msg.lower():
                return "The AI service is currently unavailable. Please try again later."
            elif "quota" in error_msg.lower() or "limit" in error_msg.lower():
                return "API usage limit reached. Please try again later."
            else:
                return f"I encountered an error while processing your question: {error_msg}"
    
    def get_document_type(self, document_text: str) -> str:
        """
        Identify the type of legal document
        
        Args:
            document_text: The extracted text from the legal document
            
        Returns:
            Identified document type
        """
        prompt = f"""
        Analyze this legal document and identify what type of document it is. 
        Provide a brief classification (e.g., "Rental Agreement", "Employment Contract", 
        "Terms of Service", "Loan Agreement", etc.)
        
        Document text (first 1000 characters):
        {document_text[:1000]}
        
        Document type:
        """
        
        try:
            response = self.model.generate_content(prompt)
            if response.text:
                return response.text.strip()
            else:
                return "Unknown Document Type"
        except Exception as e:
            return "Unknown Document Type"
