import threading
import time
from search import search_prompt

FRAMES = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]

STAGES = [
    (0.0,  "🔍 Estou buscando os dados"),
    (1.2,  "🤔 Estou pensando"),
    (2.4,  "🔢 Estou calculando"),
]


def _loading(stop: threading.Event) -> None:
    start = time.time()
    i = 0
    while not stop.is_set():
        elapsed = time.time() - start
        label = STAGES[0][1]
        for threshold, msg in STAGES:
            if elapsed >= threshold:
                label = msg
        print(f"\r{label} {FRAMES[i % len(FRAMES)]}   ", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print("\r" + " " * 50 + "\r", end="", flush=True)


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

            stop = threading.Event()
            loader = threading.Thread(target=_loading, args=(stop,), daemon=True)
            loader.start()

            print("\nAssistente: ", end="", flush=True)
            first = True
            for chunk in chain.stream(question):
                if first:
                    stop.set()
                    loader.join()
                    print("\nAssistente: ", end="", flush=True)
                    first = False
                print(chunk, end="", flush=True)
            print()

        except (KeyboardInterrupt, EOFError):
            print("\n\nEncerrando chat. Até logo!")
            break
        except Exception as e:
            print(f"\nErro ao processar pergunta: {e}")


if __name__ == "__main__":
    main()
