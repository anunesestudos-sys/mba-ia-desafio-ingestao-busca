"""Unit tests for ingest_pdf using mocks (no DB / API needed)."""
import sys
import os
import pytest
from unittest.mock import patch, MagicMock
from langchain_core.documents import Document

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import ingest


class TestIngestPdfValidation:
    def test_exits_when_pdf_path_not_set(self, monkeypatch):
        monkeypatch.setattr(ingest, "PDF_PATH", "")
        monkeypatch.setattr(ingest, "DATABASE_URL", "postgresql+psycopg://x")
        with pytest.raises(SystemExit):
            ingest.ingest_pdf()

    def test_exits_when_database_url_not_set(self, monkeypatch):
        monkeypatch.setattr(ingest, "PDF_PATH", "doc.pdf")
        monkeypatch.setattr(ingest, "DATABASE_URL", "")
        with pytest.raises(SystemExit):
            ingest.ingest_pdf()

    @patch("ingest.PGVector")
    @patch("ingest.GoogleGenerativeAIEmbeddings")
    @patch("ingest.PyPDFLoader")
    def test_full_ingest_calls_pipeline(self, mock_loader, mock_embed, mock_pgvector, monkeypatch):
        monkeypatch.setattr(ingest, "PDF_PATH", "doc.pdf")
        monkeypatch.setattr(ingest, "DATABASE_URL", "postgresql+psycopg://fake")

        mock_loader.return_value.load.return_value = [
            Document(page_content="A" * 2000, metadata={"source": "doc.pdf"})
        ]
        mock_pgvector.from_documents = MagicMock()

        ingest.ingest_pdf()

        mock_loader.assert_called_once_with("doc.pdf")
        mock_pgvector.from_documents.assert_called_once()

    @patch("ingest.PGVector")
    @patch("ingest.GoogleGenerativeAIEmbeddings")
    @patch("ingest.PyPDFLoader")
    def test_chunks_respect_size_limit(self, mock_loader, mock_embed, mock_pgvector, monkeypatch):
        monkeypatch.setattr(ingest, "PDF_PATH", "doc.pdf")
        monkeypatch.setattr(ingest, "DATABASE_URL", "postgresql+psycopg://fake")

        mock_loader.return_value.load.return_value = [
            Document(page_content="Word " * 1000, metadata={"source": "doc.pdf"})
        ]

        captured = {}

        def capture(**kwargs):
            captured["documents"] = kwargs.get("documents", [])

        mock_pgvector.from_documents = MagicMock(side_effect=capture)

        ingest.ingest_pdf()

        chunks = captured.get("documents", [])
        assert len(chunks) > 1
        for chunk in chunks:
            assert len(chunk.page_content) <= 1000
