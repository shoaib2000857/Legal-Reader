"""
Demo script for Legal Document Analyzer without API requirements
Tests document processing functionality
"""
import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

from src.utils.document_processor import DocumentProcessor

def demo_document_processing():
    """Demo the document processing functionality"""
    print("🏛️ Legal Document Analyzer - Demo Mode")
    print("=" * 50)
    print("Testing document processing without AI...")
    
    # Initialize document processor
    doc_processor = DocumentProcessor()
    
    # Test with sample document
    sample_file = "data/sample_documents/sample_lease_agreement.txt"
    
    try:
        # Read the sample file
        with open(sample_file, 'r', encoding='utf-8') as f:
            file_content = f.read().encode('utf-8')
        
        # Process the document
        doc_info = doc_processor.process_document(file_content, "sample_lease_agreement.txt")
        
        print("✅ Document processed successfully!")
        print(f"📄 File: {doc_info['file_name']}")
        print(f"📊 Word Count: {doc_info['word_count']:,}")
        print(f"📏 Character Count: {doc_info['character_count']:,}")
        print(f"📋 File Type: {doc_info['file_type']}")
        
        print("\n📖 Document Preview (first 500 characters):")
        print("-" * 50)
        preview = doc_info['text'][:500] + "..." if len(doc_info['text']) > 500 else doc_info['text']
        print(preview)
        
        print("\n🎯 Mock AI Analysis Results:")
        print("-" * 50)
        
        mock_analysis = {
            'summary': """
DOCUMENT SUMMARY:
This is a standard residential lease agreement between a landlord and tenant. 
The document establishes a 12-month rental term with monthly payments due on the 1st of each month. 
Key parties involved are the property owner (landlord) and the person renting the property (tenant).
Important dates include the lease start and end dates, with a 30-day notice requirement for termination.
            """.strip(),
            
            'key_terms': """
KEY TERMS & CLAUSES:
1. Monthly Rent Payment: Tenant must pay rent on the 1st day of each month
2. Late Fee Policy: $50 late fee charged after the 5th day of the month  
3. Security Deposit: Required before occupancy, used for damages beyond normal wear
4. Utilities Responsibility: Tenant pays for electricity, gas, water, sewer, trash, internet
5. Maintenance Obligations: Tenant keeps property clean, landlord handles major repairs
6. Pet Policy: No pets without written permission and additional deposit
            """.strip(),
            
            'risks': """
POTENTIAL RISKS & RED FLAGS:
⚠️ Late Fee Structure: $50 late fee after only 5 days could accumulate quickly
⚠️ Utility Costs: All utilities are tenant's responsibility - could be expensive
⚠️ Security Deposit: No specific amount mentioned - could be substantial
⚠️ Immediate Termination: Landlord can terminate immediately for lease violations
⚠️ No Pet Clause: Strict no-pet policy limits tenant flexibility
⚠️ Inspection Access: Landlord has "reasonable access" - terms not clearly defined
            """.strip(),
            
            'plain_english': """
PLAIN ENGLISH EXPLANATION:
This is a rental agreement that says:
- You're renting a place for 1 year
- You pay rent every month on the 1st
- If you're late with rent (after the 5th), you pay an extra $50
- You pay for all utilities (electric, gas, water, internet, etc.)
- You give the landlord money upfront as a security deposit
- You can't have pets unless you get special permission
- You have to keep the place clean and let the landlord in for repairs
- Either you or the landlord can end this early with 30 days notice
- If you break the rules, the landlord can kick you out immediately
            """.strip(),
            
            'action_items': """
RECOMMENDED ACTIONS BEFORE SIGNING:
✅ MUST DO:
1. Fill in all blank spaces (dates, amounts, addresses, names)
2. Clarify the exact security deposit amount
3. Get written clarification on what "reasonable access" means for inspections
4. Ask for a detailed list of what utilities you'll be responsible for
5. Request estimated monthly utility costs from previous tenants

✅ SHOULD ASK:
1. What constitutes "normal wear and tear" vs. damage?
2. How much notice is required for landlord entry?
3. What happens if you need to break the lease early?
4. Are there any restrictions on guests or overnight visitors?
5. What repairs are tenant vs. landlord responsibility?

✅ CONSIDER:
1. Negotiating the late fee amount or grace period
2. Getting renter's insurance
3. Taking photos of the property condition before moving in
4. Reading local tenant rights laws for your area

⚖️ CONSULT A LAWYER IF:
- The security deposit seems excessive
- You don't understand any terms
- You want to negotiate major changes
            """.strip()
        }
        
        for analysis_type, result in mock_analysis.items():
            print(f"\n📋 {analysis_type.upper().replace('_', ' ')}:")
            print(result)
        
        print("\n" + "=" * 50)
        print("🎉 Demo completed successfully!")
        print("\n💡 To use with real AI analysis:")
        print("1. Get a Google API key from: https://makersuite.google.com/app/apikey")
        print("2. Add it to your .env file: GOOGLE_API_KEY=your_key_here")
        print("3. Run: streamlit run app.py")
        
    except Exception as e:
        print(f"❌ Error in demo: {str(e)}")

if __name__ == "__main__":
    demo_document_processing()
