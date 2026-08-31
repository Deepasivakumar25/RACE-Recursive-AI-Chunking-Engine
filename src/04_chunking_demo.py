from pathlib import Path
import importlib.util

SRC_DIR = Path(__file__).resolve().parent


def load_module(filename: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, SRC_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pdf_extraction = load_module("02_pdf_extraction.py", "pdf_extraction")
recursive_splitter = load_module("03_recursive_text_splitter.py", "recursive_text_splitter")


def run(pdf_path: str):
    rec_pdf = pdf_extraction.extract_pdf_text(pdf_path)
    chunk_list = recursive_splitter.split_text(rec_pdf)
    print(chunk_list)
    return chunk_list
