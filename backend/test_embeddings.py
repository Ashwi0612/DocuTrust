from embeddings import create_embeddings

chunks = [
    {
        "page": 1,
        "text": "Employees receive 20 days of annual leave."
    },
    {
        "page": 2,
        "text": "The company provides medical insurance."
    }
]

embeddings = create_embeddings(chunks)

print("Number of embeddings:", len(embeddings))
print("Embedding dimension:", len(embeddings[0]))