import os
from dotenv import load_dotenv
from langchain_postgres import PGVector
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME", "rag_documents")
EMBEDDING_MODEL = os.getenv("GOOGLE_EMBEDDING_MODEL", "models/embedding-001")

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""


def _format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def search_prompt():
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)

        vectorstore = PGVector(
            embeddings=embeddings,
            collection_name=COLLECTION_NAME,
            connection=DATABASE_URL,
        )

        retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

        prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)

        chain = (
            {
                "contexto": retriever | _format_docs,
                "pergunta": RunnablePassthrough(),
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        return chain

    except Exception as e:
        print(f"Erro ao inicializar o sistema: {e}")
        return None
