from pypdf import PdfReader


def extract_pdf_text(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    rec_pdf = ""
    for rec in reader.pages:
        rec_pdf += rec.extract_text() or ""
    return rec_pdf
