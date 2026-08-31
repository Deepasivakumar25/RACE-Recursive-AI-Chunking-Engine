from pypdf import PdfReader

reader = PdfReader("Hybrid_Search_Practice.pdf")
rec_pdf = ""

for rec in reader.pages:
    rec_pdf += rec.extract_text()
