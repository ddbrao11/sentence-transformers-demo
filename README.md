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

