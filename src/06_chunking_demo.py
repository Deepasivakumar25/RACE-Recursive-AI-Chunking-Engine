from pathlib import Path
import sys

SRC_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC_DIR))

# This module mirrors the final notebook step that creates chunks.
# Import the splitter module directly when using this file as a script.

def display_chunks(chunks: list[str]) -> None:
    for index, chunk in enumerate(chunks, start=1):
        print(f"Chunk {index}:\n{chunk}\n")
