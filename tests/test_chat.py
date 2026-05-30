"""Unit tests for the interactive chat loop."""
import sys
import os
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import chat


class TestChatMain:
    @patch("chat.search_prompt", return_value=None)
    def test_exits_when_chain_not_initialized(self, mock_sp, capsys):
        chat.main()
        out = capsys.readouterr().out
        assert "Não foi possível iniciar" in out

    @patch("chat.search_prompt")
    @patch("builtins.input", side_effect=["sair"])
    def test_sair_command_exits_loop(self, mock_input, mock_sp, capsys):
        mock_sp.return_value = MagicMock()
        chat.main()
        out = capsys.readouterr().out
        assert "Encerrando" in out

    @patch("chat.search_prompt")
    @patch("builtins.input", side_effect=["exit"])
    def test_exit_command_exits_loop(self, mock_input, mock_sp, capsys):
        mock_sp.return_value = MagicMock()
        chat.main()
        out = capsys.readouterr().out
        assert "Encerrando" in out

    @patch("chat.search_prompt")
    @patch("builtins.input", side_effect=["ajuda", "sair"])
    def test_help_command_shows_commands(self, mock_input, mock_sp, capsys):
        mock_sp.return_value = MagicMock()
        chat.main()
        out = capsys.readouterr().out
        assert "Comandos disponíveis" in out

    @patch("chat.search_prompt")
    @patch("builtins.input", side_effect=["", "sair"])
    def test_empty_input_is_ignored(self, mock_input, mock_sp, capsys):
        mock_chain = MagicMock()
        mock_sp.return_value = mock_chain
        chat.main()
        mock_chain.invoke.assert_not_called()

    @patch("chat.search_prompt")
    @patch("builtins.input", side_effect=["Qual empresa?", "sair"])
    def test_question_invokes_chain(self, mock_input, mock_sp, capsys):
        mock_chain = MagicMock()
        mock_chain.invoke.return_value = "Empresa Zenith"
        mock_sp.return_value = mock_chain
        chat.main()
        mock_chain.invoke.assert_called_once_with("Qual empresa?")

    @patch("chat.search_prompt")
    @patch("builtins.input", side_effect=EOFError)
    def test_eof_exits_gracefully(self, mock_input, mock_sp, capsys):
        mock_sp.return_value = MagicMock()
        chat.main()
        out = capsys.readouterr().out
        assert "Encerrando" in out
