import os
import PyPDF2
from utils import get_logger

log = get_logger("DataLoader")

class DataLoader:
    def __init__(self):
        pass

    def read_pdf(self, file_path):
        """
        Parses a PDF file and extracts text page by page.
        """
        if not os.path.exists(file_path):
            log.error(f"File not found: {file_path}")
            raise FileNotFoundError("The provided file does not exist.")

        text = ""
        try:
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                # Iterate through all pages to extract text
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text += page.extract_text() + " "
            log.info(f"Successfully read PDF: {file_path}")
        except Exception as e:
            log.error(f"Failed to read PDF. Error: {str(e)}")
            return ""

        return text

    def read_txt(self, file_path):
        """Reads a standard plain text file."""
        if not os.path.exists(file_path):
            log.error(f"File not found: {file_path}")
            raise FileNotFoundError("The txt file does not exist.")
            
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        return data

    def load_document(self, file_path):
        # Determine the correct parsing method based on the file extension
        ext = file_path.split(".")[-1].lower()
        if ext == "pdf":
            return self.read_pdf(file_path)
        elif ext == "txt":
            return self.read_txt(file_path)
        else:
            log.warning("Unsupported file type detected. Attempting to parse as plain text.")
            return self.read_txt(file_path)
