import os
import sys
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")
DATABASE_URL = os.getenv("DATABASE_URL")
COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME", "rag_documents")
EMBEDDING_MODEL = os.getenv("GOOGLE_EMBEDDING_MODEL", "models/embedding-001")


def ingest_pdf():
    """Load PDF, split into chunks of 1000 chars / 150 overlap, embed and store in PGVector."""
    if not PDF_PATH:
        print("Erro: PDF_PATH não configurado no .env")
        sys.exit(1)
    if not DATABASE_URL:
        print("Erro: DATABASE_URL não configurado no .env")
        sys.exit(1)

    print(f"Carregando PDF: {PDF_PATH}")
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()
    print(f"Páginas carregadas: {len(documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
    )
    chunks = splitter.split_documents(documents)
    print(f"Chunks gerados: {len(chunks)}")

    print("Gerando embeddings e armazenando no PostgreSQL...")
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)

    PGVector.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        connection=DATABASE_URL,
        pre_delete_collection=True,
    )

    print(f"Ingestão concluída: {len(chunks)} chunks armazenados.")


if __name__ == "__main__":
    ingest_pdf()
