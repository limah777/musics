import os
import time
from rich.console import Console
from rich.live import Live

console = Console()


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def digitar(texto, atraso, cor="white"):
    acumulado = ""
    with Live("", console=console, refresh_per_second=20, transient=True) as live:
        for caracter in texto:
            acumulado += caracter
            live.update(f"[{cor}]{acumulado}[/]")
            time.sleep(atraso)
    console.print(f"[bold {cor}]{texto}[/]")
    time.sleep(0.6)


def main():
    limpar_tela()
    digitar("E vinte e quatro horas se passaram", 0.04)
    digitar("e outra vez", 0.05)
    digitar("o sol se pôs, a lua nasceu", 0.05)
    digitar("e de novo", 0.01)
    digitar("e de novo", 0.01)
    digitar("e de novo", 0.01)
    console.print()
    digitar("O sol pediu a lua em casamento", 0.19, "yellow")
    digitar("e a lua, disse:", 0.23, "yellow")
    digitar("NÃO SEI...", 0.01, "yellow")
    digitar("NÃO SEI...", 0.01, "yellow")
    digitar("NÃO SEI...", 0.01, "yellow")
    digitar("me dá um tempo", 0.07, "yellow")
    console.print()
    digitar("o sol congelou seu coração", 0.13)
    time.sleep(2)
    console.print()
    limpar_tela()


if __name__ == "__main__":
    main()
