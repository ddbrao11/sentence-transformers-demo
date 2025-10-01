# 🧠 Sentence Transformers Demo: BERT-based Sentence Embeddings

This repository contains a beginner-friendly implementation of **Sentence Transformers** using the [Hugging Face `sentence-transformers`](https://www.sbert.net/) library.  
It demonstrates how to generate **sentence embeddings** and compute **semantic similarity** with just a few lines of Python code.

---

## 📌 What are Sentence Transformers?

Sentence Transformers (SBERT) build on top of **BERT and Transformer models** to generate **semantically meaningful sentence embeddings**.  
These embeddings can be used for:

- ✅ Semantic Search  
- ✅ Question Answering  
- ✅ Document Clustering  
- ✅ Recommendation Systems  
- ✅ Chatbots (RAG – Retrieval Augmented Generation)  

---

## 📂 Repository Structure

```
sentence-transformers-demo/
│── README.md        # Project overview + instructions
│── requirements.txt # Dependencies
│── main.py          # Example script (run from CLI)
│── notebook.ipynb   # Jupyter Notebook with step-by-step demo
```

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/sentence-transformers-demo.git
cd sentence-transformers-demo

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Quickstart

### ▶️ Run from Command Line
```bash
python main.py
```

Expected Output (example):
```
--- Pairwise similarity demo ---
Pairwise similarity between:
  'I love playing football.'
  'Soccer is my favorite sport.'
→ 0.7201

--- Semantic search demo (top-3) ---
Query: How to fix a punctured bike tire?
  1. (score: 0.8123) Best ways to repair a flat bike tire.
  2. (score: 0.7954) How do I replace a punctured bicycle tire?
  3. (score: 0.5122) Steps to change a car tire.

Query: I want to learn about AI vs machine learning
  1. (score: 0.8411) What is the difference between AI and machine learning?
  2. (score: 0.5302) Where to learn Python programming.
  3. (score: 0.4215) Deep learning and neural networks are part of AI.
```

*(Note: Scores may vary slightly depending on environment & model version)*

---

### 📓 Run Jupyter Notebook
Start Jupyter Notebook:
```bash
jupyter notebook notebook.ipynb
```

You’ll see:
- Embedding shapes (vector size: 384 for `all-MiniLM-L6-v2`)  
- Pairwise semantic similarity scores across example sentences  
- Semantic search retrieving the top-k most similar corpus items  

---

## 🔎 Semantic Search Mini-Demo

This repo includes a simple semantic search demo that:
- Encodes a small corpus of sentences into embeddings.
- Encodes user query(ies) into embeddings.
- Uses `sentence_transformers.util.semantic_search` to retrieve the top-k most semantically similar corpus sentences.

Run it:
```bash
python main.py
```

The script prints pairwise similarity examples and the top-3 search results for sample queries.

---

## 📊 Example Similarity Scores

| Sentence A                           | Sentence B                               | Similarity |
|--------------------------------------|------------------------------------------|------------|
| I love playing football.             | Soccer is my favorite sport.              | 0.72       |
| Artificial intelligence is transforming the world. | Deep learning and neural networks are part of AI. | 0.68       |

---

## 🏗️ Models Covered

This demo uses **`all-MiniLM-L6-v2`** (lightweight, fast, accurate).  

Other popular embedding models you can try:
- **`paraphrase-MiniLM-L6-v2`** – optimized for paraphrase mining.  
- **`all-mpnet-base-v2`** – more accurate but heavier.  
- **OpenAI `text-embedding-ada-002`** – widely used in industry (API-based).  
- **Cohere / Google Vertex AI Embeddings** – production-ready embedding APIs.  

---

## 📌 Resources

- [Sentence Transformers Official Docs](https://www.sbert.net/)  
- [Hugging Face Model Hub](https://huggingface.co/models)  
- [Introduction to Semantic Search](https://www.sbert.net/examples/applications/semantic-search/README.html)  

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork, open issues, or submit PRs.

---

## 📜 License

This project is released under the MIT License.
