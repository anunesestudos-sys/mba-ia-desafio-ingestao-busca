"""Unit tests for search_prompt initialization and error handling."""
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import search


class TestSearchPromptInit:
    @patch("search.ChatGoogleGenerativeAI")
    @patch("search.PGVector")
    @patch("search.GoogleGenerativeAIEmbeddings")
    def test_returns_chain_on_success(self, mock_embed, mock_pgvec, mock_llm, monkeypatch):
        monkeypatch.setattr(search, "DATABASE_URL", "postgresql+psycopg://fake")

        mock_vs = MagicMock()
        mock_vs.as_retriever.return_value = MagicMock()
        mock_pgvec.return_value = mock_vs

        chain = search.search_prompt()
        assert chain is not None

    @patch("search.GoogleGenerativeAIEmbeddings")
    @patch("search.PGVector", side_effect=Exception("DB connection failed"))
    def test_returns_none_on_db_error(self, mock_pgvec, mock_embed, monkeypatch):
        monkeypatch.setattr(search, "DATABASE_URL", "postgresql+psycopg://fake")

        chain = search.search_prompt()
        assert chain is None

    @patch("search.ChatGoogleGenerativeAI")
    @patch("search.PGVector")
    @patch("search.GoogleGenerativeAIEmbeddings")
    def test_retriever_uses_k_equals_10(self, mock_embed, mock_pgvec, mock_llm, monkeypatch):
        monkeypatch.setattr(search, "DATABASE_URL", "postgresql+psycopg://fake")

        mock_vs = MagicMock()
        mock_pgvec.return_value = mock_vs

        search.search_prompt()
        mock_vs.as_retriever.assert_called_once_with(search_kwargs={"k": 10})
