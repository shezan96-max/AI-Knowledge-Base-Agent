import faiss
import pickle
import os
import numpy as np
from app.core.embeddings import embed_texts,embed_query


class VectorStore:
    def __init__(self):
        self.index = None
        self.text_chunks = []

    def build(self,texts):
        vectors = embed_texts(texts)
        dim = vectors.shape[1]

        self.index = faiss.IndexFlatL2(dim)
        self.index.add(vectors)

        self.text_chunks = texts

    def search(self,query,top_k):
        query_vector = embed_query(query).reshape(1,-1)
        results = []

        distances,indices = self.index.search(query_vector,top_k)

        for i,idx in enumerate(indices[0]):
            results.append({
                "text" : self.text_chunks[idx],
                "distance" : float(distances[0][i])
            })

        return results
    
    def save(self):
        os.makedirs("vector_db",exist_ok=True)

        faiss.write_index(self.index, "vector_db/index.faiss")

        with open("vector_db/texts.pkl","wb") as f:
            pickle.dump(self.text_chunks,f)

    def load(self):
        if not os.path.exists("vector_db/index.faiss"):
            return False
        self.index = faiss.read_index("vector_db/index.faiss")

        with open("vector_db/texts.pkl","rb") as f:
            self.text_chunks = pickle.load(f)

        return True