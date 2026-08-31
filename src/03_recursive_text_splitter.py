from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(rec_pdf: str, chunk_size: int = 500, chunk_overlap: int = 100) -> list[str]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return text_splitter.split_text(rec_pdf)
