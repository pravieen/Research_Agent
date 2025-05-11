# Personal Research Assistant

A powerful research assistant that helps you analyze academic papers using AI.

## Features

- Search for academic papers on any topic
- AI-powered paper summarization
- Cross-paper synthesis and analysis
- Clean and intuitive Streamlit interface

## Architecture

- Backend: FastAPI + LangChain + Gemini
- Frontend: Streamlit
- Data Sources: arXiv API

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure API keys:
- Add your Gemini API key to `configs/secrets.yml`

3. Run the application:

Start the backend server:
```bash
python main.py
```

In a new terminal, start the Streamlit frontend:
```bash
streamlit run streamlit_app.py
```

## Best Practices

- Clean code architecture with separation of concerns
- Comprehensive error handling
- Caching for API responses
- Modular and reusable components
- Clear documentation

## System Design

The application follows a microservices architecture:
1. FastAPI backend handles paper fetching and AI processing
2. Streamlit frontend provides user interface
3. Caching layer for improved performance
4. AI layer for paper analysis using Gemini

## Challenges and Solutions

1. PDF Processing
   - Challenge: Extracting text from PDFs reliably
   - Solution: Used pdfplumber with robust error handling

2. API Rate Limits
   - Challenge: arXiv API limitations
   - Solution: Implemented caching system

3. Large Text Processing
   - Challenge: Processing long papers with AI
   - Solution: Chunking and efficient text processing

4. User Experience
   - Challenge: Making complex functionality accessible
   - Solution: Clean Streamlit interface with progress indicators