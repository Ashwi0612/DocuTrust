from embeddings import create_embeddings
from vector_store import create_vector_store, search

print("Creating sample chunks...")

chunks = [
    {
        "page": 1,
        "text": "Employees receive 20 days of annual leave."
    },
    {
        "page": 2,
        "text": "Medical insurance is provided."
    },
    {
        "page": 3,
        "text": "Employees work five days a week."
    }
]

print("Creating embeddings...")
embeddings = create_embeddings(chunks)

print("Creating vector store...")
create_vector_store(chunks, embeddings)

print("Creating query embedding...")
query = [
    {
        "page": 0,
        "text": "How many leave days are allowed?"
    }
]

query_embedding = create_embeddings(query)

print("Searching...")
results = search(query_embedding)

print("\nResults:")
for result in results:
    print(result)