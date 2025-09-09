# Legal Reader 🏛️

**AI-Powered Legal Document Analyzer**

Legal Reader is an intelligent web application that uses Google's Gemini AI to simplify complex legal documents into clear, accessible guidance. It empowers users to understand their legal documents, identify potential risks, and make informed decisions.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.29+-red.svg)

## 🎯 Problem Statement

Legal documents—such as rental agreements, loan contracts, and terms of service—are often filled with complex, impenetrable jargon that is incomprehensible to the average person. This creates a significant information asymmetry, where individuals may unknowingly agree to unfavorable terms, exposing them to financial and legal risks.

## 🚀 Solution

Legal Reader bridges this gap by providing:

- **📋 Document Summaries**: Clear, concise summaries of complex legal documents
- **🔑 Key Terms Analysis**: Important clauses explained in plain English
- **⚠️ Risk Detection**: Identification of potential red flags and unfavorable terms
- **💬 Plain English Translation**: Complex legal language simplified
- **✅ Action Items**: Specific recommendations before signing
- **💬 Interactive Q&A**: Chat interface to ask questions about your document

## 🌟 Features

### Core Functionality
- **Multi-format Support**: Upload PDF, DOCX, or TXT files
- **AI-Powered Analysis**: Uses Google Gemini Pro for comprehensive document analysis
- **Interactive Chat**: Ask specific questions about your document
- **Risk Assessment**: Identifies potential legal and financial risks
- **Document Statistics**: Visual representation of document metrics
- **Report Generation**: Download comprehensive analysis reports

### User Experience
- **Intuitive Interface**: Clean, easy-to-use web interface
- **Real-time Processing**: Fast document analysis and response
- **Privacy-Focused**: Documents are not stored or shared
- **Mobile Responsive**: Works on desktop and mobile devices

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: Google Gemini Pro API
- **Document Processing**: PyPDF2, python-docx
- **Visualization**: Plotly
- **Backend**: Python 3.8+

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Google API key for Gemini Pro

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/shoaib2000857/Legal-Reader.git
   cd Legal-Reader
   ```

2. **Run the setup script**
   ```bash
   ./setup.sh
   ```

3. **Get your Google API key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the API key

4. **Configure your environment**
   ```bash
   # Edit the .env file and add your API key
   GOOGLE_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   source legal_reader_env/bin/activate
   streamlit run app.py
   ```

### Manual Installation

If you prefer manual installation:

```bash
# Create virtual environment
python -m venv legal_reader_env
source legal_reader_env/bin/activate  # On Windows: legal_reader_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env and add your Google API key

# Run the application
streamlit run app.py
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Required
GOOGLE_API_KEY=your_google_api_key_here

# Optional (for future enhancements)
OPENAI_API_KEY=your_openai_key_here
```

### API Key Setup

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the generated key
4. Add it to your `.env` file

## 📖 Usage

### Basic Workflow

1. **Upload Document**: Click "Choose a file" and select your legal document
2. **Document Processing**: The system will extract and analyze the text
3. **Start Analysis**: Click "Start AI Analysis" to begin comprehensive analysis
4. **Review Results**: Navigate through different analysis tabs:
   - **Summary**: Overview of the document
   - **Key Terms**: Important clauses explained
   - **Risks & Red Flags**: Potential concerns
   - **Plain English**: Simplified explanation
   - **Action Items**: What to do before signing
5. **Ask Questions**: Use the chat interface for specific queries
6. **Download Report**: Get a comprehensive analysis report

### Supported Document Types

- **Rental/Lease Agreements**
- **Employment Contracts**
- **Loan Agreements**
- **Terms of Service**
- **Privacy Policies**
- **Purchase Agreements**
- **Service Contracts**
- **NDAs & Confidentiality Agreements**

### Supported File Formats

- **PDF** (.pdf)
- **Microsoft Word** (.docx)
- **Plain Text** (.txt)

## 📁 Project Structure

```
Legal-Reader/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── setup.sh                       # Setup script
├── .env.example                   # Environment variables template
├── src/
│   ├── utils/
│   │   ├── document_processor.py  # Document text extraction
│   │   └── ai_analyzer.py         # AI analysis engine
│   └── components/
│       └── ui_components.py       # Streamlit UI components
├── data/
│   └── sample_documents/          # Sample legal documents
│       ├── sample_lease_agreement.txt
│       └── sample_loan_agreement.txt
└── README.md
```

## 🔒 Privacy & Security

- **No Data Storage**: Documents are processed in memory and not saved
- **Secure Processing**: All communication with AI services is encrypted
- **Session-Based**: Each session is independent and private
- **Local Processing**: Document text extraction happens locally

## ⚖️ Legal Disclaimer

**Important**: This tool provides general information and should not replace professional legal advice. Always consult with a qualified attorney for important legal matters. The AI analysis is for informational purposes only and may not catch all potential issues in a legal document.

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google for providing the Gemini Pro API
- Streamlit for the excellent web framework
- The open-source community for various libraries used

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/shoaib2000857/Legal-Reader/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your setup and the issue

## 🚀 Future Enhancements

- [ ] Multi-language support
- [ ] Integration with more AI models
- [ ] Advanced document comparison features
- [ ] Legal precedent database integration
- [ ] Mobile app version
- [ ] Batch document processing
- [ ] Legal template generation

---

**Made with ❤️ for making legal documents accessible to everyone**