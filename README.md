# Sanskrit_Rag-Project

Project Overview

This project implements an end-to-end Retrieval-Augmented Generation (RAG) system for answering queries based on Sanskrit documents, developed as part of a company-assigned technical assessment.

The system retrieves relevant context from Sanskrit texts and generates coherent, context-grounded answers using a CPU-only Large Language Model (LLM). The entire pipeline is executed locally using VS Code, with clear modular separation between retrieval and generation components.

Objectives

Build a complete RAG pipeline for Sanskrit documents
Support user queries in Sanskrit (and transliterated Sanskrit)
Ensure CPU-only inference (no GPU usage)
Maintain modular, readable, and reproducible code
Demonstrate sound ML engineering practices under constraints


System Architecture

The system follows standard RAG principles with the following flow:
Document Loading
Preprocessing & Chunking
Vector Embedding Generation
Vector-based Retrieval (FAISS)
Context-Aware Answer Generation


Sanskrit Documents

Source: Sanskrit documents provided by the company
Format: .txt (UTF-8 encoded)
Content Type: Classical Sanskrit prose and narrative texts
External Data: ❌ Not used

No labeled datasets were required, as the task focuses on retrieval and generation rather than supervised training.

Project Structure
RAG_Sanskrit_<YourName>/
│
├── code/
│   ├── config.py
│   ├── loader.py
│   ├── preprocess.py
│   ├── embedder.py
│   ├── retriever.py
│   ├── generator.py
│   └── main.py
│
├── data/
│   └── sanskrit_docs.txt
│
├── report/
│   └── Sanskrit_RAG_Technical_Report.pdf
│
├── requirements.txt
└── README.md

Environment & Constraints

Python: 3.9+
Execution Mode: CPU-only
GPU / CUDA: Disabled
IDE: VS Code
Final Execution: Local machine (not Google Colab)
CUDA usage is explicitly disabled and verified during execution.

Installation & Setup
1. Clone the Repository
git clone <your-repo-url>
cd RAG_Sanskrit_<YourName>

2. Create Virtual Environment
python -m venv rag_env

3. Activate Environment
Windows (PowerShell / VS Code terminal):
rag_env\Scripts\activate

4. Install Dependencies
pip install -r requirements.txt

Running the System
From the project root:

cd code
python main.py


On startup, the system:

Loads Sanskrit documents
Preprocesses and chunks text
Builds embeddings and retrieval index
Starts an interactive query loop

You will see:
System ready. Ask questions in Sanskrit (type 'exit' to quit).
