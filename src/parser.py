import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from PDF. For scanned PDFs, integrate OCR (e.g., pytesseract).
    """
    text_pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text_pages.append(page.extract_text() or '')
    return '\n'.join(text_pages)