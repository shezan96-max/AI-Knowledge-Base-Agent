# AI Knowledge Base Agent

AI Powered chatbot that answers questions from company documents and captures leads automatically.

## Features 
- RAG bases AI chatbot
- Knowledge upload system
- Lead capture automation
- Email notifications
- Analytics dashboard
- Intent detection


## Tech Stack
FastAPI
FAISS
Sentence Transformers
PostgreSQL
Streamlit

## System Architecture
User - Streamlit UI - FastAPI - RAG Engine - Vector DB - Database

## How to Run
1. Start backend
uvicorn app.main:app --reload

2. Start UI
streamlit run ui/app.py
