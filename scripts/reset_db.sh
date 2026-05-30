#!/usr/bin/env bash
# Limpa todos os chunks armazenados no PostgreSQL
set -e
source "$(dirname "$0")/../venv/bin/activate"
cd "$(dirname "$0")/.."

source .env
DB_URL=$(echo "$DATABASE_URL" | sed 's|postgresql+psycopg://|postgresql://|')

echo "Limpando coleção: $PG_VECTOR_COLLECTION_NAME"
psql "$DB_URL" -c "
  DELETE FROM langchain_pg_embedding e
  USING langchain_pg_collection c
  WHERE c.uuid = e.collection_id AND c.name = '$PG_VECTOR_COLLECTION_NAME';
  DELETE FROM langchain_pg_collection WHERE name = '$PG_VECTOR_COLLECTION_NAME';
"
echo "✅ Banco limpo. Execute 'python src/ingest.py' para re-ingerir."
