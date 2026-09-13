# AI Resume-to-Job Fit Analyzer

This repository contains the implementation of my course project for Fundamentals in AI & ML. The project is a localized NLP-based tool designed to evaluate the compatibility between a candidate's resume and a target job description.

## Overview
Many qualified applicants are rejected by automated Applicant Tracking Systems (ATS) due to missing keywords. This tool simulates an ATS by analyzing the text of a resume against a job description. It calculates a mathematical matching score and identifies critical keywords that the applicant should consider adding before applying.

## Key Features
- **Custom NLP Pipeline**: Implements Term Frequency-Inverse Document Frequency (TF-IDF) and Cosine Similarity entirely from scratch using Python and NumPy, avoiding heavy pre-packaged machine learning libraries.
- **Actionable Feedback**: Outputs the specific missing keywords to help improve the resume.
- **Data Privacy**: All files are processed locally in-memory, ensuring personal resume data is never transmitted to external servers.
- **Multi-format Support**: Successfully parses text from both `.txt` and `.pdf` files.

## Technologies Used
- **Python 3** (Core programming language)
- **NumPy** (For mathematical vector operations)
- **PyPDF2** (For parsing PDF documents)
- **Git & GitHub** (For version control)

## Installation and Execution

1. **Clone the Repository**
   ```bash
   git clone https://github.com/adilsukumar/ATS_Resume-to-Job_Fit_Analyzer.git
   cd ATS_Resume-to-Job_Fit_Analyzer
   ```

2. **Environment Setup (Recommended)**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python main.py --jd sample_jd.txt --resume sample_resume.txt
   ```

## Instructions for Testing
The project includes automated validation unit tests for the core mathematical models to ensure accuracy.
To run the tests yourself, execute:
```bash
python -m unittest test_model.py
```
*(The test results are also logged in `test_execution_proof.txt`.)*

## Screenshots
Below is an example of the terminal output when executing the pipeline:

*(Optional: Execution screenshots can be uploaded here)*
