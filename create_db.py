import os

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    Docx2txtLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# -----------------------------
# Configuration
# -----------------------------
DATA_FOLDER = "data"
CHROMA_DB_DIR = "chroma_db"

# -----------------------------
# Load all text documents
# -----------------------------
documents = []

print("Loading knowledge files...\n")

for filename in os.listdir(DATA_FOLDER):
     
    file_path = os.path.join(DATA_FOLDER, filename)

    print(f"Reading: {filename}")

    # Choose the correct loader
    if filename.endswith(".txt"):
      loader = TextLoader(file_path)

    elif filename.endswith(".pdf"):
      loader = PyPDFLoader(file_path)

    elif filename.endswith(".docx"):
      loader = Docx2txtLoader(file_path)

    else:
        continue
    docs = loader.load()
    
    documents.extend(docs)

print(f"\nTotal files loaded: {len(documents)}")

# -----------------------------
# Split documents into chunks
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Total chunks created: {len(chunks)}")

# -----------------------------
# Create embedding model
# -----------------------------
embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)

# -----------------------------
# Create Chroma Database
# -----------------------------
Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=CHROMA_DB_DIR
)

print("\nDatabase created successfully!")