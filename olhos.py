import os
import time
from rich.console import Console
from rich.live import Live

console = Console()


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def digitar(texto, atraso, cor="white"):
    exibido = ""
    with Live("", console=console, refresh_per_second=20, transient=True) as live:
        for caracter in texto:
            exibido += caracter
            live.update(f"[{cor}]{exibido}[/]")
            time.sleep(atraso)
    console.print(f"[bold {cor}]{texto}[/]")
    time.sleep(0.6)


def main():
    limpar_tela()
    digitar("No meu pensamento eu sei que vai ficar", 0.06)
    time.sleep(0.3)
    digitar("A todo momento, sei que vou lembrar", 0.08)
    digitar("Do brilho dos teus olhos", 0.08)
    console.print()
    time.sleep(2.3)
    digitar("Fecho os olhos, não consigo te esquecer", 0.07, "blue")
    digitar("Tem alguém comigo, mas não é você", 0.08)
    time.sleep(0.6)
    digitar("Tenho até medo de dormir, pra não lembrar", 0.07)
    console.print()
    time.sleep(0.7)
    digitar("Daqueles olhos (aqueles olhos), aqueles olhos (inconfundíveis olhos)", 0.07, "blue")
    digitar("Aqueles olhos, que refletem luz no meu coração", 0.15)
    console.print()
    digitar("Aqueles olhos (aqueles olhos), aqueles olhos (inconfundíveis olhos)", 0.09, "blue")
    digitar("Aqueles olhos, que refletem luz no meu coração", 0.15)
    console.print()
    time.sleep(2)
    limpar_tela()


if __name__ == "__main__":
    main()
    
