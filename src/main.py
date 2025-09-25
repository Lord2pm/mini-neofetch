import typer
import platform
import psutil
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()


@app.command()
def info():
    """Exibe informações do sistema (similar ao neofetch)."""
    uname = platform.uname()

    table = Table(title="Mini Neofetch", title_style="bold cyan")

    table.add_column("Categoria", style="magenta", no_wrap=True)
    table.add_column("Informação", style="green")

    table.add_row("Sistema", f"{uname.system} {uname.release}")
    table.add_row("Kernel", uname.version)
    table.add_row("Arquitetura", uname.machine)
    table.add_row("Processador", uname.processor or "N/A")

    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()

    table.add_row("CPU", f"{cpu_cores} núcleos / {cpu_threads} threads")
    if cpu_freq:
        table.add_row("Frequência", f"{cpu_freq.current:.2f} MHz")

    mem = psutil.virtual_memory()
    table.add_row(
        "Memória", f"{mem.used // (1024**2)} MB / {mem.total // (1024**2)} MB"
    )

    disk = psutil.disk_usage("/")
    table.add_row(
        "Disco", f"{disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB"
    )

    console.print(table)


@app.command()
def ascii():
    """Mostra um ASCII art simples."""
    logo = """
      ███╗   ██╗███████╗ ██████╗ ███████╗
      ████╗  ██║██╔════╝██╔═══██╗██╔════╝
      ██╔██╗ ██║█████╗  ██║   ██║███████╗
      ██║╚██╗██║██╔══╝  ██║   ██║╚════██║
      ██║ ╚████║███████╗╚██████╔╝███████║
      ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝
    """
    console.print(logo, style="bold cyan")


if __name__ == "__main__":
    app()
