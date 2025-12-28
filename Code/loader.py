from pathlib import Path

def load_documents(data_dir):
    texts = []
    for file in Path(data_dir).glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            texts.append(f.read())
    return texts
