---

# 📄 Resume AI Parser

A Python-based tool to **parse resumes (PDFs)**, store **job postings**, and (later) perform **resume-job matching with relevance scoring**.

---

## 🚀 Features

### ✅ Current

* **PDF → Text Conversion**

  * Extracts text from text-based resumes (Word, Canva, etc.).
  * Saves extracted text into `.txt` and logs it in the console.

* **Job Posting Manager**

  * Add job postings interactively via console prompts.
  * Auto-generates **Position Codes** (`POS-001`, `POS-002`, etc.).
  * Stores all postings in `data/job_postings.json`.
  * Handles empty or corrupted JSON files gracefully.

### 🔜 Upcoming

* Keyword-based matching between resumes and job postings with a **score out of 100**.
* View, edit, and delete job postings.
* CLI-based interactive menu or GUI.

---

## 🗂️ Project Structure

```
resume_parser/
├── data/
│   ├── pdfs/                 # Input resumes
│   ├── extracted_texts/      # Extracted text files
│   ├── job_postings.json     # Stored job postings
├── src/
│   ├── pdf_to_text.py        # PDF to text logic
│   ├── job_posting_manager.py# Job postings logic
├── main.py                   # Entry point
└── requirements.txt
```

---

## ⚙️ Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd resume_parser
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure Folders Exist**

   ```
   data/pdfs
   data/extracted_texts
   ```

---

## ▶️ Usage

### **1. PDF → Text Conversion**

* Place resumes inside `data/pdfs/`.
* Run:

  ```bash
  python main.py
  ```
* Output text will be saved in `data/extracted_texts/<filename>.txt` and printed in the console.

---

### **2. Add Job Postings**

* Run:

  ```bash
  python main.py
  ```

* Follow prompts:

  ```
  === ADD A NEW JOB POSTING ===
  Enter Position Name: Software Engineer
  Enter Job Description: Responsible for building scalable systems
  Enter Experience Required (in years): 3
  Enter Specific Skills: Python, Django, REST API
  Enter Context Sentences: good in coding, international ranking of 900 or above
  ✅ Job Posting Added Successfully! Position Code: POS-001
  ```

* Check `data/job_postings.json` for stored postings.

---

## 📌 Example JSON Output

```json
[
  {
    "position_code": "POS-001",
    "position_name": "Software Engineer",
    "description": "Responsible for building scalable systems",
    "experience_required": "3",
    "skills": ["Python", "Django", "REST API"],
    "context_sentences": ["good in coding", "international ranking of 900 or above"]
  }
]
```

---

## 🛠️ Next Steps

* [ ] Add keyword-based matching & scoring logic.
* [ ] Add job postings viewer and editor.
* [ ] Make an interactive CLI menu.

---

## 👨‍💻 Author

**Prasidham Sinha**

---

✅ **Copy-paste this as `README.md` in your project root**, and it will display perfectly on GitHub.

---

### 🔥 **Next Suggestion**

Would you like me to now:
✅ **write a `.gitignore` (to keep your repo clean)**, or
✅ **start building the interactive menu (Add / View / Exit jobs)?**
