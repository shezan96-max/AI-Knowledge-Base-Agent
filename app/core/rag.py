from app.core.chunker import chunk_text
from app.core.vector_store import VectorStore
from app.core.llm import ask_llm
import os

def build_knowledge_base(file_path):
    if not os.path.exists(file_path):
        raise Exception("File not found")

    with open(file_path,"r",encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)
    store = VectorStore()
    store.build(chunks)

    store.save()
    return store
def load_knowledge_base():
    store = VectorStore()
    store.load()
    return store

def retrieve_context(question,store):
    results = store.search(question,top_k=3)
    context = "\n\n".join([r["text"] for r in results])
    return context

def run_rag(question,store):
    context = retrieve_context(question,store)

    prompt = f"""
You are an AI Assistant for a business.
Answer ONLY using the provided context.
Be short and professional and do not include anything extra unless asked.

Context:
{context}

Question:
{question}

Answer:
"""
    try:
        answer = ask_llm(prompt)
        return answer
    except Exception as e:
        print("LLM Error:",e)