from transformers import pipeline


def load_generator(model_name):
    return pipeline(
        "text2text-generation",
        model=model_name,
        device=-1
    )


def generate_answer(generator, context, query):
    MAX_CONTEXT_CHARS = 1500
    context = context[:MAX_CONTEXT_CHARS]

    prompt = f"""
उत्तरं संस्कृतेन देहि।

सन्दर्भः:
{context}

प्रश्नः:
{query}

उत्तरम्:
"""

    output = generator(
        prompt,
        max_new_tokens=128,    
        do_sample=False,       
        num_beams=1,            
        truncation=True
    )

    return output[0]["generated_text"]
