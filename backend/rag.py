import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
for m in client.models.list():
    print(m.name)


def generate_answer(question, context):
    return f"""
Answer (RAG Demo Mode):

Based on the uploaded document, here is the relevant information:

{context[:800]}

Question:
{question}
"""

    response = client.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=prompt
    )

    return response.text