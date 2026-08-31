# Install FAISS in Google Colab:
# !pip install -q accelerate faiss-cpu

import faiss
import numpy as np

embedding_dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(embedding_dimension)
index.add(embeddings)

question = "what is mean by hybrid search?"
question_embedding = embedding_model.encode([question])

distance, index_number = index.search(
    np.array(question_embedding),
    k=5
)

retrieved_chunks = [chunk_list[rec] for rec in index_number[0]]
