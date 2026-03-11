from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    return model.encode(texts,convert_to_numpy=True)

def embed_query(query):
    return embed_texts([query])[0]

    