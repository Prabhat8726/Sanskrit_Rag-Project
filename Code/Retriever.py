import faiss
import numpy as np

class Retriever:
    def __init__(self, embeddings):
        self.dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dim)
        self.index.add(embeddings.astype("float32"))

    def search(self, query_embedding, top_k):
        distances, indices = self.index.search(
            query_embedding.astype("float32"), top_k
        )
        return indices[0]
