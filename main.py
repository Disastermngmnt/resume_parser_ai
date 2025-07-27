# ================================
# main.py
# ================================

from src.pdf_to_text import pdf_to_text

if __name__ == "__main__":
    # Give the path to your sample PDF
    pdf_path = "data/pdfs/prasitest.pdf"
    
    # Call the function to convert PDF to text
    text_file = pdf_to_text(pdf_path)
    print(f"Text saved at: {text_file}")
