from search import search_prompt


def main():
    """Start the interactive RAG chat loop. Type 'sair' or Ctrl+C to exit."""
    print("=" * 60)
    print("  RAG Chat - Consulta de Documentos PDF")
    print("=" * 60)
    print("Inicializando sistema...")

    chain = search_prompt()

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    print("Sistema pronto! Faça sua pergunta.")
    print("Comandos: 'sair' para encerrar, 'ajuda' para mais opções.")
    print("-" * 60)

    while True:
        try:
            question = input("\nVocê: ").strip()

            if not question:
                continue

            if question.lower() in ("exit", "quit", "sair"):
                print("Encerrando chat. Até logo!")
                break

            if question.lower() in ("help", "ajuda"):
                print("\nComandos disponíveis:")
                print("  sair / exit  - Encerra o chat")
                print("  ajuda / help - Exibe esta mensagem")
                continue

            print("\nAssistente: ", end="", flush=True)
            response = chain.invoke(question)
            print(response)

        except (KeyboardInterrupt, EOFError):
            print("\n\nEncerrando chat. Até logo!")
            break
        except Exception as e:
            print(f"\nErro ao processar pergunta: {e}")


if __name__ == "__main__":
    main()
