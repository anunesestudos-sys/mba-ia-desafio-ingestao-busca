"""Tests for search module: prompt assembly and doc formatting."""
import sys
import os
import pytest
from unittest.mock import MagicMock
from langchain_core.documents import Document

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from search import _format_docs, PROMPT_TEMPLATE


class TestFormatDocs:
    def test_single_doc_returns_content(self):
        docs = [Document(page_content="Hello world")]
        result = _format_docs(docs)
        assert result == "Hello world"

    def test_multiple_docs_joined_by_double_newline(self):
        docs = [
            Document(page_content="First chunk"),
            Document(page_content="Second chunk"),
        ]
        result = _format_docs(docs)
        assert result == "First chunk\n\nSecond chunk"

    def test_empty_docs_list_returns_empty_string(self):
        result = _format_docs([])
        assert result == ""

    def test_preserves_whitespace_in_content(self):
        docs = [Document(page_content="  spaced  content  ")]
        result = _format_docs(docs)
        assert result == "  spaced  content  "


class TestPromptTemplate:
    def test_template_contains_context_placeholder(self):
        assert "{contexto}" in PROMPT_TEMPLATE

    def test_template_contains_question_placeholder(self):
        assert "{pergunta}" in PROMPT_TEMPLATE

    def test_template_contains_out_of_context_rule(self):
        assert "Não tenho informações necessárias" in PROMPT_TEMPLATE

    def test_template_forbids_external_knowledge(self):
        assert "conhecimento externo" in PROMPT_TEMPLATE

    def test_prompt_fills_correctly(self):
        from langchain_core.prompts import PromptTemplate
        prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
        filled = prompt.format(contexto="Empresa Zenith", pergunta="Qual empresa?")
        assert "Empresa Zenith" in filled
        assert "Qual empresa?" in filled
