def chunk_document(pages, chunk_size=500, overlap=100):
    """
    Split extracted PDF text into overlapping chunks.
    """

    chunks = []

    for page in pages:

        text = page["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk = text[start:end]

            chunks.append({
                "page": page["page"],
                "text": chunk
            })

            start += chunk_size - overlap

    return chunks