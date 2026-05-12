import os
import time
from rich.console import Console
from rich.live import Live

console = Console()


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def digitar(texto, atraso, cor="white"):
    linha = ""
    with Live("", console=console, refresh_per_second=20, transient=True) as live:
        for caracter in texto:
            linha += caracter
            live.update(f"[{cor}]{linha}[/]")
            time.sleep(atraso)
    console.print(f"[bold {cor}]{texto}[/]")
    time.sleep(0.6)


def main():
    limpar_tela()
    digitar("Diga pra mim que é real", 0.11, "blue")
    time.sleep(1.5)
    digitar("Que eu te prometo meu melhor", 0.12)
    time.sleep(0.9)
    digitar("Fala pra mim o que eu quero ouvir", 0.09, "blue")
    time.sleep(0.7)
    digitar("Que tu sentiu o que eu senti", 0.1)
    time.sleep(0.9)
    console.print()
    digitar("Me diga agora, por favor (me diga agora, por favor)", 0.09, "blue")
    digitar("Que eu vou correndo te abraçar (que eu vou correndo-)", 0.08)
    time.sleep(1)
    time.sleep(2)
    limpar_tela()


if __name__ == "__main__":
    main()
