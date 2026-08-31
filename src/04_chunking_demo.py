from pathlib import Path
import sys

SRC_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC_DIR))

from 02_pdf_extraction import extract_pdf_text
from 03_recursive_text_splitter import split_text


def run(pdf_path: str):
    rec_pdf = extract_pdf_text(pdf_path)
    chunk_list = split_text(rec_pdf)
    print(chunk_list)
    return chunk_list
