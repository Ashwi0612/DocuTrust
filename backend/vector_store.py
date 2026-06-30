import faiss
import numpy as np

# Global variables
index = None
stored_chunks = []


def create_vector_store(chunks, embeddings):
    """
    Create FAISS index and store document chunks.
    """

    global index, stored_chunks

    if len(embeddings) == 0:
        raise ValueError("No embeddings provided")

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    stored_chunks = chunks


def search(query_embedding, k=3):
    """
    Search top-k relevant chunks.
    """

    global index, stored_chunks

    if index is None:
        raise ValueError("FAISS index not initialized. Upload a PDF first.")

    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []

    for idx in indices[0]:
        if 0 <= idx < len(stored_chunks):
            results.append(stored_chunks[idx])

    return results