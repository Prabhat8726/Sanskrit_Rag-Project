from sentence_transformers import SentenceTransformer

def load_embedder(model_name):
    return SentenceTransformer(model_name)

def embed_texts(model, texts):
    return model.encode(texts, show_progress_bar=True)
