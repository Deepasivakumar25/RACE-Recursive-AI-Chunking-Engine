from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
scores = model.predict(context_list)
print(scores)

sorted_idx = np.argsort(scores)[::-1]
print(sorted_idx)

best_cross_encoders_chunks = []
for idx in sorted_idx[:3]:
    best_cross_encoders_chunks.append(unique_list_text[idx])

context = "\n\n".join(best_cross_encoders_chunks)
