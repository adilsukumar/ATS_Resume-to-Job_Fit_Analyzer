# AI Resume-to-Job Fit Analyzer

This repository contains the implementation of my course project for Artificial Intelligence and Machine Learning. The project is a localized NLP-based tool designed to evaluate the compatibility between a candidate's resume and a target job description.

## Overview
Many qualified applicants are rejected by automated Applicant Tracking Systems (ATS) due to missing keywords. This tool simulates an ATS by analyzing the text of a resume against a job description. It calculates a matching score and identifies critical keywords that the applicant should consider adding.

## Key Features
- **Custom NLP Pipeline**: Implements Term Frequency-Inverse Document Frequency (TF-IDF) and Cosine Similarity entirely from scratch using NumPy.
- **Actionable Feedback**: Outputs the specific missing keywords to help improve the resume.
- **Data Privacy**: All files are processed locally on the machine, ensuring personal data is not transmitted to external servers.
- **Multi-format Support**: Successfully parses text from both `.txt` and `.pdf` files.

## Technologies Used
- **Python 3** (Core programming language)
- **NumPy** (For mathematical vector operations)
- **PyPDF2** (For parsing PDF documents)
- **Git & GitHub** (For version control and code hosting)

## Installation and Execution

1. **Clone the Repository**
   `git clone https://github.com/adilsukumar/ATS_Resume-to-Job_Fit_Analyzer.git`
   `cd ATS_Resume-to-Job_Fit_Analyzer`

2. **Environment Setup**
   It is recommended to use a virtual environment:
   `python -m venv venv`
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`

3. **Install Dependencies**
   `pip install -r requirements.txt`

4. **Run the Application**
   `python main.py --jd target_job.txt --resume my_resume.pdf`

## Testing Instructions
The project includes automated validation unit tests for the core mathematical models.
To run the tests, execute:
`python -m unittest test_model.py`
The test results are also logged in `test_execution_proof.txt`.

## Screenshots
*(Optional: Execution screenshots can be uploaded here)*

---

## Technical Evaluation Criteria
- **Modular Implementation**: The system is structured into 6 distinct Python modules (`main.py`, `utils.py`, `data_loader.py`, `features.py`, `model.py`, and `test_model.py`), fulfilling the 5-10 module requirement.
- **Validation**: Automated unit testing is implemented using Python's `unittest` framework to validate the TF-IDF and Cosine Similarity algorithms.
- **Subject Concepts**: Successfully applies foundational AI algorithms (TF-IDF and Cosine Similarity) using vector mathematics.
- **Documentation**: Includes comprehensive inline code comments, design diagrams, and a structured `statement.md`.
- **Error Handling**: Utilizes `try-except` blocks to handle file reading errors and unsupported formats gracefully.
- **Version Control**: Developed using Git with consistent commit history.

## Non-Functional Requirements (NFRs)
- **Performance**: Utilizes vectorized operations via NumPy for efficient scoring.
- **Security**: Local processing ensures zero external API exposure.
- **Usability**: Features a straightforward Command-Line Interface (CLI).
- **Reliability**: Implements fallback mechanisms for file parsing errors.
- **Logging**: Execution details are logged to `app_debug.log` for troubleshooting.
