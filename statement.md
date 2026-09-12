# Project Statement

## Problem Statement
Job seekers and university students frequently face rejection from automated Applicant Tracking Systems (ATS) due to a lack of keyword optimization in their resumes. Because the screening process is automated, qualified candidates are often filtered out before their applications are reviewed by human recruiters.

## Scope of the Project
This project focuses on building a local, offline command-line tool that performs textual comparison between a job description and a resume. The scope is limited to utilizing Term Frequency-Inverse Document Frequency (TF-IDF) and Cosine Similarity to generate a match percentage and identify missing keywords. The scope does not include automated job applications or web scraping.

## Target Users
- **University Students**: Seeking to optimize their resumes for campus placements.
- **Job Seekers**: Preparing tailored applications for specific roles.
- **Career Advisors**: Assisting candidates in identifying skill gaps.

## High-Level Features
1. **Document Loading**: Capable of parsing both `.txt` and `.pdf` files securely.
2. **Text Normalization**: Cleans raw text by removing punctuation, standardizing case, and filtering stop-words.
3. **Feature Extraction**: Constructs a custom TF-IDF vocabulary from the input corpus using mathematical foundations.
4. **Similarity Scoring**: Calculates the Cosine Similarity metric between the generated document vectors.
5. **Feedback Generation**: Identifies and displays the most critical missing keywords from the resume.
