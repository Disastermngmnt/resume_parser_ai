import os
import PyPDF2

"""
     pdf_to_text Converts a PDF to plain text and saves it as a .txt file.
    
    Args:
        pdf_path (str): The full path to the PDF file.
        output_folder (str): The folder where the text file will be saved.

    Returns:
        str: The path of the generated text file.
"""
def pdf_to_text(pdf_path: str, output_folder="data/extracted_texts"):
     
    # 1. Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # 2. Get only file_name ( resume.pdf -> 'resume')
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # 3. Full path for the output text file
    text_file_path = os.path.join(output_folder, f"{file_name}.txt")

    # 3. Open the PDF file in 'read-binary' mode (rb)
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)   # Create a PDF reader object
        extracted_text = ""                   # Empty string to collect all text
       
        # Loop through all pages in the PDF
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]     # Get each page one by one
            text = page.extract_text()        # Extract text from the page
            
            if text:                          # Add only if text is found
                extracted_text += text + "\n\n"
    # 4. Save the extracted text to a .txt file
    with open(text_file_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(extracted_text)
    
    print(f"✅ Text extracted and saved to: {text_file_path}")
    return text_file_path