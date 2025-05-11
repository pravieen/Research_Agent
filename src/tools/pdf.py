import requests
import pdfplumber
import os
from tempfile import NamedTemporaryFile


def download_and_extract_pdf(pdf_url: str) -> str:
    print("📥 Downloading PDF...")
    response = requests.get(pdf_url)

    with NamedTemporaryFile(suffix=".pdf", delete=False) as tmpfile:
        tmpfile.write(response.content)
        tmpfile_path = tmpfile.name

    print("📄 Extracting text from PDF...")
    text = ""
    try:
        with pdfplumber.open(tmpfile_path) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"
                if i % 5 == 0:
                    print(f"Read page {i + 1}...")
    finally:
        os.unlink(tmpfile_path)  # Clean up temp file

    print(f"🧾 Extracted {len(text)} characters")
    return text