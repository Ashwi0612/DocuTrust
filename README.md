# DocuTrust — AI Document Intelligence System

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Frontend-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

---

## Overview

DocuTrust is an AI-powered document intelligence system that allows users to upload PDF files and interact with their content using natural language queries.

The system extracts text from documents, processes it using AI models, and returns context-aware responses to user questions in real time.

---

## Features

- PDF document upload and processing
- AI-based question answering over documents
- Efficient text extraction and parsing
- REST API-based backend architecture
- Simple and responsive web interface
- Real-time interaction with AI model

---

## Tech Stack

**Frontend**
- HTML5
- CSS3
- JavaScript

**Backend**
- Python
- FastAPI / Flask
- REST APIs

**AI Integration**
- Google GenAI / OpenAI API
- NLP-based document understanding

---

## Project Structure
```
DocuTrust/
│
├── backend/                 # Backend API (FastAPI / Flask)
│   ├── main.py              # Entry point
│   ├── utils.py             # Helper functions
│   ├── requirements.txt     # Dependencies
│   └── config.py            # Configuration settings
│
├── frontend/                # UI layer
│   ├── index.html           # Main interface
│   ├── style.css            # Styling
│   ├── script.js            # Frontend logic
│
├── uploads/                 # Uploaded PDFs storage
├── static/                  # Static assets (optional)
├── .gitignore               # Ignored files
├── README.md                # Project documentation
└── LICENSE                  # License file
---
```
## Installation

### Clone repository
```bash
git clone https://github.com/YOUR_USERNAME/DocuTrust.git
cd DocuTrust
```

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend
```bash
frontend/index.html
```
in a browser.

---
## System Workflow

1. User uploads a PDF document
2. Backend extracts and preprocesses text
3. AI model processes document content
4. User submits a query via UI
5. System returns context-aware response
---

## Future Enhancements

1. Authentication and user management system
2. Cloud deployment (AWS / Azure / Render)
3. Multi-document conversational memory
4. Document summarization module
5. Analytics dashboard for uploaded files
---

## Project Purpose

This project demonstrates practical implementation of:

- Full-stack web development
- AI integration with real-world applications
- Document processing pipelines
- REST API design and usage

---
## Author

Ashwitha M
---
