#!/usr/bin/env bash
set -e

echo "=== Setup RAG Desafio 01 ==="

# 1. venv
if [ ! -d "venv" ]; then
  echo "[1/4] Criando venv..."
  python3 -m venv venv
fi
source venv/bin/activate

# 2. dependências
echo "[2/4] Instalando dependências..."
pip install --quiet langchain langchain-community langchain-postgres \
  langchain-google-genai psycopg psycopg-binary pgvector pypdf \
  python-dotenv openai sqlalchemy asyncpg pytest pytest-cov

# 3. .env
if [ ! -f ".env" ]; then
  echo "[3/4] Criando .env a partir do exemplo..."
  cp .env.example .env
  echo "  ⚠️  Edite .env e preencha GOOGLE_API_KEY e DATABASE_URL"
else
  echo "[3/4] .env já existe, pulando."
fi

# 4. testes unitários
echo "[4/4] Rodando testes unitários..."
python -m pytest tests/ -v --ignore=tests/test_integration.py \
  --ignore=tests/test_performance.py -q

echo ""
echo "✅ Setup concluído!"
echo ""
echo "Próximos passos:"
echo "  1. Edite .env com suas chaves"
echo "  2. Suba o PostgreSQL: ssh minha-vps 'cd ~/rag-desafio && docker compose up -d'"
echo "  3. Ingira o PDF: python src/ingest.py"
echo "  4. Inicie o chat: python src/chat.py"
