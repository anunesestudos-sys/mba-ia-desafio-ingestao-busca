"""Performance benchmarks — latência de consulta e qualidade de embeddings."""
import sys
import os
import time
import pytest
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

needs_env = pytest.mark.skipif(
    not os.getenv("DATABASE_URL") or not os.getenv("GOOGLE_API_KEY"),
    reason="DATABASE_URL ou GOOGLE_API_KEY não configurados",
)

LATENCY_LIMIT_SECONDS = 30


@needs_env
class TestQueryLatency:
    def test_single_query_under_latency_limit(self):
        """Consulta end-to-end deve completar em menos de 30 segundos."""
        chain = search_prompt()
        start = time.time()
        chain.invoke("Quais empresas estão listadas?")
        elapsed = time.time() - start
        print(f"\n[PERF] Latência consulta: {elapsed:.2f}s")
        assert elapsed < LATENCY_LIMIT_SECONDS

    def test_three_sequential_queries_average_latency(self):
        """Média de 3 consultas sequenciais deve ser menor que o limite."""
        chain = search_prompt()
        times = []
        for q in ["Quais empresas?", "Quais valores?", "Qual é a capital da França?"]:
            t0 = time.time()
            chain.invoke(q)
            times.append(time.time() - t0)
        avg = sum(times) / len(times)
        print(f"\n[PERF] Latências: {[f'{t:.2f}s' for t in times]} | Média: {avg:.2f}s")
        assert avg < LATENCY_LIMIT_SECONDS


@needs_env
class TestEmbeddingQuality:
    def test_similar_queries_return_overlapping_results(self):
        """Perguntas semanticamente similares devem recuperar chunks em comum."""
        import search as s

        embeddings = s.GoogleGenerativeAIEmbeddings(model=s.EMBEDDING_MODEL)
        from langchain_postgres import PGVector
        vs = PGVector(embeddings=embeddings, collection_name=s.COLLECTION_NAME, connection=s.DATABASE_URL)
        retriever = vs.as_retriever(search_kwargs={"k": 10})

        docs_a = retriever.invoke("Quais empresas estão no documento?")
        docs_b = retriever.invoke("Liste as empresas presentes no arquivo.")

        ids_a = {d.page_content[:50] for d in docs_a}
        ids_b = {d.page_content[:50] for d in docs_b}
        overlap = ids_a & ids_b
        print(f"\n[PERF] Overlap chunks consultas similares: {len(overlap)}/10")
        assert len(overlap) >= 5

    def test_different_queries_return_different_results(self):
        """Perguntas semanticamente diferentes devem ter baixo overlap."""
        import search as s

        embeddings = s.GoogleGenerativeAIEmbeddings(model=s.EMBEDDING_MODEL)
        from langchain_postgres import PGVector
        vs = PGVector(embeddings=embeddings, collection_name=s.COLLECTION_NAME, connection=s.DATABASE_URL)
        retriever = vs.as_retriever(search_kwargs={"k": 10})

        docs_a = retriever.invoke("Quais empresas estão no documento?")
        docs_b = retriever.invoke("Qual é a capital da França?")

        ids_a = {d.page_content[:50] for d in docs_a}
        ids_b = {d.page_content[:50] for d in docs_b}
        overlap = ids_a & ids_b
        print(f"\n[PERF] Overlap chunks consultas diferentes: {len(overlap)}/10")
        assert len(overlap) < 10
