"""Integration tests — require real DB and Google API (skipped when env vars absent)."""
import sys
import os
import pytest
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

SKIP_REASON = "DATABASE_URL ou GOOGLE_API_KEY não configurados"
needs_env = pytest.mark.skipif(
    not os.getenv("DATABASE_URL") or not os.getenv("GOOGLE_API_KEY"),
    reason=SKIP_REASON,
)


@needs_env
class TestSearchIntegration:
    def test_query_in_context_returns_answer(self):
        """Pergunta no contexto deve retornar resposta com dados reais."""
        from search import search_prompt
        chain = search_prompt()
        assert chain is not None
        response = str(chain.invoke("Quais empresas estão listadas no documento?"))
        assert len(response) > 10
        assert "Não tenho informações" not in response

    def test_query_out_of_context_returns_standard_message(self):
        """Pergunta fora do contexto deve retornar a frase padrão do PRD."""
        from search import search_prompt
        chain = search_prompt()
        response = str(chain.invoke("Qual é a capital da França?"))
        assert "Não tenho informações necessárias" in response

    def test_multiple_questions_in_sequence(self):
        """Múltiplas perguntas em sequência devem retornar respostas válidas."""
        from search import search_prompt
        chain = search_prompt()
        questions = [
            "Quais valores aparecem no documento?",
            "Qual é a capital da França?",
            "Quais empresas são mencionadas?",
        ]
        for q in questions:
            r = str(chain.invoke(q))
            assert isinstance(r, str) and len(r) > 0

    def test_fabricated_question_is_refused(self):
        """Sistema não deve inventar dados ausentes do contexto."""
        from search import search_prompt
        chain = search_prompt()
        response = str(chain.invoke("Quantos funcionários tem a empresa Zenith em 2030?"))
        assert "Não tenho informações necessárias" in response

    def test_ingest_pipeline_stores_67_chunks(self):
        """Ingestão do document.pdf deve armazenar exatamente 67 chunks."""
        import psycopg
        db_url = os.getenv("DATABASE_URL", "").replace("postgresql+psycopg://", "postgresql://")
        conn = psycopg.connect(db_url)
        cur = conn.cursor()
        cur.execute(
            "SELECT COUNT(*) FROM langchain_pg_embedding e "
            "JOIN langchain_pg_collection c ON c.uuid = e.collection_id "
            "WHERE c.name = %s",
            (os.getenv("PG_VECTOR_COLLECTION_NAME", "rag_documents"),),
        )
        count = cur.fetchone()[0]
        conn.close()
        assert count == 67
