import os
import sys

try:
    from art import text2art
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.align import Align
except ImportError:
    print("Required packages are missing.")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)

def main():
    # Retrieve the environment variables
    param1 = os.environ.get('PARAMETER1')
    param2 = os.environ.get('PARAMETER2')

    # Check if both parameters are provided
    if param1 is None or param2 is None:
        console = Console()
        console.print("[bold red]Error:[/] Please set both [bold cyan]PARAMETER1[/] and [bold cyan]PARAMETER2[/] environment variables.")
        console.print("\n[bold yellow]Example usage:[/]")
        console.print("  [green]export[/] PARAMETER1='First'")
        console.print("  [green]export[/] PARAMETER2='Second'")
        console.print("  [green]python[/] fancy_print.py")
        sys.exit(1)

    console = Console()

    # Generate ASCII art using the 'art' library
    # 'block' and 'cybermedium' are examples of cool fonts
    art1 = text2art(param1, font="block")
    art2 = text2art(param2, font="cybermedium")

    # Wrap the ASCII art in beautiful styled panels using 'rich'
    panel1 = Panel(
        Align.center(Text(art1, style="bold cyan")),
        title="[bold yellow]✨ PARAMETER 1 ✨[/bold yellow]",
        border_style="cyan",
        padding=(1, 4),
        expand=False
    )

    panel2 = Panel(
        Align.center(Text(art2, style="bold magenta")),
        title="[bold green]🚀 PARAMETER 2 🚀[/bold green]",
        border_style="magenta",
        padding=(1, 4),
        expand=False
    )

    # Print a nice empty line before and after
    console.print()
    console.print(Align.center(panel1))
    console.print()
    console.print(Align.center(panel2))
    console.print()

if __name__ == "__main__":
    main()
