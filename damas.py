import os
import time
from rich.console import Console
from rich.live import Live

console = Console()


def limpar_tela():
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)


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
    digitar("Prometo que eu vou tentar te deixar menos nervosa", 0.04, "yellow")
    digitar("E quando fizer merda, compro dois buquê de rosas", 0.05)
    console.print()
    digitar("E se ainda assim tiver nervosa, minha rainha inconstante", 0.04, "yellow")
    time.sleep(0.1)
    digitar("Session de massoterapia com incenso hidratante", 0.04)
    console.print()
    time.sleep(0.1)
    digitar("Te prometo cada batida do meu coração", 0.05, "yellow")
    digitar("Prometo, teremos problemas, mas nunca sem solução", 0.05)
    console.print()
    digitar("Promessas à parte, ficaremos sempre assim", 0.05, "yellow")
    digitar("Eu gostando de você e você gostando de mim", 0.06)
    time.sleep(2)
    limpar_tela()


if __name__ == "__main__":
    main()
    
