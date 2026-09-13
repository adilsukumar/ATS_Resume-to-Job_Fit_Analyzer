# AI Resume-to-Job Fit Analyzer

Hey! This is my course project for my Fundamentals in AI & ML class. 

## Overview
Getting past automated Applicant Tracking Systems (ATS) is brutally hard for students these days. I built this local, offline command-line tool to help solve that problem. It acts just like a corporate ATS—you feed it your resume and a job description, and it uses Natural Language Processing (NLP) to calculate a match score. It even tells you exactly which keywords you are missing so you can fix your resume before you apply!

## Features
- **Built from scratch:** I didn't use any heavy "black-box" ML libraries like scikit-learn. I wrote the TF-IDF and Cosine Similarity math entirely from scratch using NumPy.
- **Finds missing keywords:** It actually shows you the specific words you need to add to your resume.
- **100% Private:** It runs completely locally in your computer's RAM, so your private resume data is never sent to the internet.
- **Reads PDFs and Text:** It can extract text from both `.pdf` and `.txt` files automatically.

## Technologies Used
- **Python 3:** The core language I used.
- **NumPy:** Used for all the high-performance vector math (dot products, magnitudes).
- **PyPDF2:** Used to rip the raw text out of PDF files.
- **Git & GitHub:** Used for version control.

## How to Install & Run

1. **Clone the repo to your computer:**
   ```bash
   git clone https://github.com/adilsukumar/ATS_Resume-to-Job_Fit_Analyzer.git
   cd ATS_Resume-to-Job_Fit_Analyzer
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the tool!**
   Just pass your job description and resume files into the command line like this:
   ```bash
   python main.py --jd sample_jd.txt --resume sample_resume.txt
   ```

## Instructions for Testing
I wrote automated unit tests using Python's built-in `unittest` framework to make sure my math engine wasn't hallucinating. 
You can run the tests yourself with:
```bash
python -m unittest test_model.py
```
*(The test results are also logged in `test_execution_proof.txt` if you want to check them out.)*

## Screenshots
Here is what it looks like when you run the tool in the terminal:

*(Add your terminal screenshot here!)*
