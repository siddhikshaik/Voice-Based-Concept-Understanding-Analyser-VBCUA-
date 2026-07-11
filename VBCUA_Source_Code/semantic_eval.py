from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_score(text, reference):

    if not text or not reference:
        return 0

    emb1 = model.encode(text, convert_to_tensor=True)
    emb2 = model.encode(reference, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2).item()

    return round(max(0, score) * 120, 2)