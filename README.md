# sentence-transformers-demo
sentence-transformers-demo
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
sentence-transformers-demo/

│── README.md # Project overview + instructions

│── requirements.txt # Dependencies

│── main.py # Example script (run from CLI)

│── notebook.ipynb # Jupyter Notebook with step-by-step demo

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/ddbrao11/sentence-transformers-demo.git
cd sentence-transformers-demo

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

🚀 Quickstart
▶️ Run from Command Line
python main.py
Expected Output:

Similarity between:
'I love playing football.'
and
'Soccer is my favorite sport.' is 0.72


(Note: Score may vary slightly depending on environment & model version)

📓 Run Jupyter Notebook

Start Jupyter Notebook:

jupyter notebook notebook.ipynb


You’ll see:

Embedding shapes (vector size: 384 for all-MiniLM-L6-v2)

Pairwise semantic similarity scores across example sentences

📊 Example Similarity Scores
Sentence A	Sentence B	Similarity
I love playing football.	Soccer is my favorite sport.	0.72
Artificial intelligence is transforming the world.	Deep learning and neural networks are part of AI.	0.68
🏗️ Models Covered

This demo uses all-MiniLM-L6-v2 (lightweight, fast, accurate).

Other popular embedding models you can try:

paraphrase-MiniLM-L6-v2 – optimized for paraphrase mining.

all-mpnet-base-v2 – more accurate but heavier.

OpenAI text-embedding-ada-002 – widely used in industry (API-based).

Cohere / Google Vertex AI Embeddings – production-ready embedding APIs.

📌 Resources

Sentence Transformers Official Docs

Hugging Face Model Hub

Introduction to Semantic Search

🤝 Contributing

Contributions are welcome! Feel free to fork, open issues, or submit PRs.

📜 License

This project is released under the MIT License.

