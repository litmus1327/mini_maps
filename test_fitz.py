import fitz

print("PyMuPDF version:", fitz.__doc__)

# Open your PDF (adjust path if needed)
pdf_path = "McLaren Fenton ED - Door Location Summary & Mini Maps 0513_25.pdf"

try:
    doc = fitz.open(pdf_path)
    print(f"Opened PDF, number of pages: {doc.page_count}")
except Exception as e:
    print("Error opening PDF:", e)
