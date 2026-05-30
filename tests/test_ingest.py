"""Tests for PDF ingestion: chunking and loading logic."""
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150


def make_splitter():
    return RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )


class TestChunking:
    def test_chunk_size_respects_limit(self):
        splitter = make_splitter()
        text = "A" * 5000
        chunks = splitter.split_text(text)
        for chunk in chunks:
            assert len(chunk) <= CHUNK_SIZE

    def test_chunk_overlap_creates_continuity(self):
        splitter = make_splitter()
        text = "X" * 3000
        chunks = splitter.split_text(text)
        assert len(chunks) > 1
        # Adjacent chunks must share content (overlap)
        for i in range(len(chunks) - 1):
            assert chunks[i][-CHUNK_OVERLAP:] == chunks[i + 1][:CHUNK_OVERLAP]

    def test_short_text_produces_single_chunk(self):
        splitter = make_splitter()
        text = "Hello world"
        chunks = splitter.split_text(text)
        assert len(chunks) == 1
        assert chunks[0] == "Hello world"

    def test_empty_text_produces_no_chunks(self):
        splitter = make_splitter()
        chunks = splitter.split_text("")
        assert chunks == []

    def test_documents_retain_metadata(self):
        splitter = make_splitter()
        doc = Document(page_content="A" * 2000, metadata={"source": "doc.pdf", "page": 1})
        chunks = splitter.split_documents([doc])
        for chunk in chunks:
            assert chunk.metadata["source"] == "doc.pdf"
            assert chunk.metadata["page"] == 1

    def test_multiple_documents_chunked_independently(self):
        splitter = make_splitter()
        docs = [
            Document(page_content="A" * 1500, metadata={"source": "a.pdf"}),
            Document(page_content="B" * 1500, metadata={"source": "b.pdf"}),
        ]
        chunks = splitter.split_documents(docs)
        sources = {c.metadata["source"] for c in chunks}
        assert "a.pdf" in sources
        assert "b.pdf" in sources
