"""
Document processor for extracting text from various file formats
"""
import PyPDF2
import docx
import io
from typing import Optional, Dict, Any


class DocumentProcessor:
    """Handles document processing and text extraction"""
    
    def __init__(self):
        self.supported_formats = {'.pdf', '.docx', '.txt'}
    
    def extract_text_from_pdf(self, file_content: bytes) -> str:
        """Extract text from PDF file"""
        try:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
    
    def extract_text_from_docx(self, file_content: bytes) -> str:
        """Extract text from DOCX file"""
        try:
            doc = docx.Document(io.BytesIO(file_content))
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text.strip()
        except Exception as e:
            raise Exception(f"Error reading DOCX: {str(e)}")
    
    def extract_text_from_txt(self, file_content: bytes) -> str:
        """Extract text from TXT file"""
        try:
            return file_content.decode('utf-8').strip()
        except Exception as e:
            raise Exception(f"Error reading TXT: {str(e)}")
    
    def process_document(self, file_content: bytes, file_name: str) -> Dict[str, Any]:
        """
        Process uploaded document and extract text
        
        Args:
            file_content: Raw file content as bytes
            file_name: Name of the uploaded file
            
        Returns:
            Dictionary with extracted text and metadata
        """
        # Get file extension
        file_extension = '.' + file_name.split('.')[-1].lower()
        
        if file_extension not in self.supported_formats:
            raise ValueError(f"Unsupported file format: {file_extension}")
        
        # Extract text based on file type
        if file_extension == '.pdf':
            text = self.extract_text_from_pdf(file_content)
        elif file_extension == '.docx':
            text = self.extract_text_from_docx(file_content)
        elif file_extension == '.txt':
            text = self.extract_text_from_txt(file_content)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
        
        return {
            'text': text,
            'file_name': file_name,
            'file_type': file_extension,
            'word_count': len(text.split()),
            'character_count': len(text)
        }
