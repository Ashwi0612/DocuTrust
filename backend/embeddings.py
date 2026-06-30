import numpy as np

def create_embeddings(texts):
    """
    Accepts: list of strings
    Returns: numpy float32 embeddings
    """

    if isinstance(texts, str):
        texts = [texts]

    # safety check
    if not isinstance(texts, list):
        raise ValueError("Input must be a list of strings")

    embeddings = []

    for text in texts:
        # ensure it's a string
        if not isinstance(text, str):
            text = str(text)

        # dummy embedding (replace with Gemini/OpenAI later)
        vec = [float(len(text))] * 384
        embeddings.append(vec)

    return np.array(embeddings).astype("float32")