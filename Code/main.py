from config import *
from loader import load_documents
from Preprocess import chunk_text
from Embedder import load_embedder, embed_texts
from Retriever import Retriever
from generator import load_generator, generate_answer
import numpy as np
import torch


def main():
    print("CUDA available:", torch.cuda.is_available())

    print("Loading documents...")
    docs = load_documents("../Data/Sanskrit_docs")

    if len(docs) == 0:
        raise ValueError("No documents loaded. Check the data folder.")

    print("Chunking...")
    chunks = []
    for d in docs:
        chunks.extend(chunk_text(d, CHUNK_SIZE, CHUNK_OVERLAP))

    print(f"Total chunks created: {len(chunks)}")

    if len(chunks) == 0:
        raise ValueError("No chunks created. Check chunking logic or input files.")

    print("Embedding...")
    embedder = load_embedder(EMBEDDING_MODEL)
    embeddings = embed_texts(embedder, chunks)

    embeddings = np.array(embeddings)

    if embeddings.ndim != 2:
        raise ValueError(f"Embeddings shape invalid: {embeddings.shape}")

    retriever = Retriever(embeddings)
    generator = load_generator(GENERATION_MODEL)

    print("System ready. Ask questions in Sanskrit (type 'exit' to quit).")

    while True:
        query = input("\nप्रश्नं लिखत: ")
        if query.lower() == "exit":
            break

        q_emb = embedder.encode([query])
        idxs = retriever.search(np.array(q_emb), TOP_K)

        context = "\n".join([chunks[i] for i in idxs])
        answer = generate_answer(generator, context, query)

        print("\nउत्तरः:\n", answer)


if __name__ == "__main__":
    main()
