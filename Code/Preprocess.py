def chunk_text(text, chunk_size, overlap):
    words = text.split()
    chunks = []

    step = chunk_size - overlap
    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i+chunk_size])
        if len(chunk.strip()) > 0:
            chunks.append(chunk)

    return chunks
