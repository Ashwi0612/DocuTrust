# DocuTrust — AI Document Intelligence System

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-AI-4285F4?style=for-the-badge&logo=google&logoColor=white)

---

## Overview

DocuTrust is an AI-powered document intelligence system that enables users to upload PDF documents and interact with them using natural language. The application extracts document content, processes it using generative AI, and delivers context-aware answers through an intuitive web interface.

---

## Features

- AI-powered question answering over PDF documents
- Intelligent document text extraction
- Natural language interaction
- FastAPI REST backend
- Responsive frontend built with HTML, CSS and JavaScript
- Real-time communication between frontend and backend

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, FastAPI |
| AI | Google Gemini API |
| Document Processing | PyMuPDF / PDF Processing Libraries |
| Communication | REST APIs |

---

## Project Structure

```text
DocuTrust/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── uploads/
│   └── ...
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/DocuTrust.git
cd DocuTrust
```

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Launch the Frontend

Open `frontend/index.html` in your preferred web browser.

---

## Workflow

1. Upload a PDF document.
2. The backend extracts and processes the document text.
3. The AI model indexes the extracted content.
4. Submit questions through the web interface.
5. Receive context-aware answers generated from the uploaded document.

---

## Future Enhancements

- User authentication
- Multi-document conversations
- Document summarization
- Cloud deployment
- Citation support for AI responses

---

## Author

**Ashwitha M**
