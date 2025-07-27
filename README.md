# Resume AI Parser

A Python-based tool to parse resumes (PDFs), extract text, and (later) match them against job postings to generate a relevance score.

---

## 🚀 Features (Current & Upcoming)
### ✅ Current
- Extracts text from text-based PDF resumes (created in Word, Canva, etc.).
- Saves the extracted text into a clean `.txt` file.

### 🔜 Upcoming
- Job posting management (with keywords and references).
- Keyword-based matching between resumes and job postings.
- Generates a match score out of 100.

---

## 🗂️ Project Structure

resume_parser/
│
├── data/ # Stores input PDFs & extracted text
│ ├── pdfs/ # Input resumes (PDF format)
│ ├── extracted_texts/ # Output text files after conversion
│
├── src/ # Source code
│ ├── pdf_to_text.py # PDF → Text converter
│
├── main.py # Entry point to run the program
├── requirements.txt # Python dependencies
└── README.md # Project documentation
