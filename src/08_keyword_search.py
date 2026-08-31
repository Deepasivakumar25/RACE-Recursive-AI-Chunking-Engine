# Install scikit-learn in Google Colab:
# !pip install -q scikit-learn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(chunk_list)
question_tfidf = vectorizer.transform([question])
similarity_scores = cosine_similarity(question_tfidf, X)

top_k = 5
top_indices = np.argsort(similarity_scores[0])[::-1][:top_k]
keyword_chunk = [chunk_list[rec] for rec in top_indices]
keyword_indices = top_indices.tolist()
semantic_indices = index_number[0].tolist()

print(keyword_indices, semantic_indices)

combined_indices = keyword_indices + semantic_indices
unique_list = list(dict.fromkeys(combined_indices))
print(unique_list)

unique_list_text = [chunk_list[rec] for rec in unique_list]
context_list = [[question, chunk_list[rec]] for rec in unique_list]
print(context_list)
