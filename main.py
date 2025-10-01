"""
main.py
Simple demo for Sentence Transformers:
1. Pairwise similarity example
2. Small semantic search demo (retrieve top-k similar sentences)
"""

from sentence_transformers import SentenceTransformer, util

def pairwise_similarity_demo(model):
    sentences = [
        "I love playing football.",
        "Soccer is my favorite sport.",
        "Artificial intelligence is transforming the world.",
        "Deep learning and neural networks are part of AI.",
        "How to fix a bike tire?"
    ]

    # Encode sentences to embeddings (tensor for util.pytorch_cos_sim)
    embeddings = model.encode(sentences, convert_to_tensor=True)

    # Pairwise example: compare index 0 and 1
    score = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    print(f"Pairwise similarity between:\n  '{sentences[0]}'\n  '{sentences[1]}'\n→ {score.item():.4f}\n")

def semantic_search_demo(model, top_k=3):
    # Corpus of documents / sentences
    corpus = [
        "How do I replace a punctured bicycle tire?",
        "Best ways to repair a flat bike tire.",
        "Tips for maintaining your bicycle chain.",
        "Where to learn Python programming.",
        "What is the difference between AI and machine learning?",
        "Steps to change a car tire.",
        "Soccer techniques for beginners."
    ]

    # Query
    queries = [
        "How to fix a punctured bike tire?",
        "I want to learn about AI vs machine learning"
    ]

    # Encode corpus and queries (convert_to_tensor recommended for util.semantic_search)
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
    query_embeddings = model.encode(queries, convert_to_tensor=True)

    # semantic_search returns a list (for each query) of hit dicts: {"corpus_id": int, "score": float}
    hits = util.semantic_search(query_embeddings, corpus_embeddings, top_k=top_k)

    # Print results
    for q_index, query in enumerate(queries):
        print(f"\nQuery: {query}")
        for rank, hit in enumerate(hits[q_index], start=1):
            corpus_id = hit['corpus_id']
            score = hit['score']
            print(f"  {rank}. (score: {score:.4f}) {corpus[corpus_id]}")

def main():
    print("Loading model 'all-MiniLM-L6-v2' (this may take a moment)...")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    print("\n--- Pairwise similarity demo ---")
    pairwise_similarity_demo(model)

    print("\n--- Semantic search demo (top-3) ---")
    semantic_search_demo(model, top_k=3)

if __name__ == "__main__":
    main()
