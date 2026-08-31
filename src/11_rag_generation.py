prompt = f"""
<|user|>

Use ONLY the context below.

Context:

{context}

Question:

{question}

If the answer is not present, reply exactly:

I couldn't find that information.

<|assistant|>
"""

response = chatbot(
    prompt,
    max_new_tokens=120,
    do_sample=False,
    return_full_text=False
)

answer = response[0]["generated_text"].strip()
print(answer)
