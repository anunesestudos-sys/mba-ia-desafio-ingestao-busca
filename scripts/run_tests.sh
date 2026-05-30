#!/usr/bin/env bash
# Roda suite completa de testes com cobertura
set -e
source "$(dirname "$0")/../venv/bin/activate"
cd "$(dirname "$0")/.."

echo "=== Testes Unitários ==="
python -m pytest tests/test_ingest.py tests/test_ingest_unit.py \
  tests/test_search.py tests/test_search_unit.py tests/test_chat.py \
  -v --cov=src --cov-report=term-missing

echo ""
echo "=== Testes de Integração (requer DB e API) ==="
python -m pytest tests/test_integration.py -v

echo ""
echo "=== Benchmarks de Performance ==="
python -m pytest tests/test_performance.py -v -s
