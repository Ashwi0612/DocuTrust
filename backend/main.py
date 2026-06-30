from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

from backend.pdf_reader import extract_text_from_pdf
from backend.chunker import chunk_document
from backend.embeddings import create_embeddings
from backend.vector_store import create_vector_store, search
from backend.rag import generate_answer

app = FastAPI(
    title="DocuTrust API",
    description="Enterprise RAG Platform",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "../uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Welcome to DocuTrust!",
        "status": "Backend is running successfully."
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Step 1: Extract text
    pages = extract_text_from_pdf(file_path)

    # Step 2: Chunk
    chunks = chunk_document(pages)

    # Step 3: Embeddings
    texts = [chunk["text"] for chunk in chunks]
    embeddings = create_embeddings(texts)

    # Step 4: Store in FAISS
    create_vector_store(chunks, embeddings)

    return {
        "filename": file.filename,
        "pages": len(pages),
        "chunks_created": len(chunks),
        "status": "upload_success"
    }


@app.post("/ask")
async def ask_question(request: QuestionRequest):

    try:
        logs = []

        logs.append("Step 1: Query received")

        # Step 1: Embed query
        query_embedding = create_embeddings([request.question])
        logs.append("Step 2: Embedding generated")

        # Step 2: Retrieve chunks
        relevant_chunks = search(query_embedding)
        logs.append("Step 3: FAISS retrieval done")

        # Step 3: Simple CRAG check (self-correction)
        def is_relevant(chunks):
            return chunks and any(len(c["text"]) > 50 for c in chunks)

        if not is_relevant(relevant_chunks):
            logs.append("Step 4: Weak results detected → refining query")

            refined_query = " ".join(request.question.split()[:5])
            query_embedding = create_embeddings([refined_query])
            relevant_chunks = search(query_embedding)

        else:
            logs.append("Step 4: Results are relevant")

        # Step 4: Sort context
        context_chunks = sorted(
            relevant_chunks,
            key=lambda x: x.get("page", 0)
        )

        context = "\n\n".join(
            f"[Page {c.get('page', 'unknown')}] {c['text']}"
            for c in context_chunks
        )

        logs.append("Step 5: Context built")

        # Step 5: Generate answer
        answer = generate_answer(request.question, context)
        logs.append("Step 6: Answer generated")

        # Step 6: Citations
        citations = sorted({
            f"Page {c.get('page', 'unknown')}"
            for c in relevant_chunks
        })

        logs.append("Step 7: Citations added")

        return {
            "question": request.question,
            "answer": answer,
            "citations": citations,
            "logs": logs,
            "status": "success"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))