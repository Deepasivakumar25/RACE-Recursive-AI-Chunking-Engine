# Install the embedding dependency in Google Colab:
# !pip install -q sentence-transformers

from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embeddings = embedding_model.encode(chunk_list)
