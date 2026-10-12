# -*- coding: utf-8 -*-
"""About action — project info, features, requirements for Crypto Clipper."""

from rich.table import Table
from rich.panel import Panel
from rich import box

from hooks.ui import console


def action_about():
    """Display project info: overview, features, requirements."""
    features_table = Table(
        show_header=True,
        header_style="bold bright_magenta",
        border_style="magenta",
        box=box.SIMPLE,
        title="[bold bright_magenta] ◈ FEATURES ◈ [/]",
        title_style="bright_magenta",
    )
    features_table.add_column("Feature", style="bright_magenta")
    features_table.add_column("Status", justify="center", style="bright_green")

    for feat in [
        "Real-time clipboard monitoring with polling",
        "Multi-chain address pattern recognition",
        "Bitcoin — Legacy, SegWit, Taproot detection",
        "Ethereum — EVM address with EIP-55 checksum",
        "Solana — Base58 address detection",
        "Tron — Base58 (T-prefix) detection",
        "Address book with chain-labeled entries",
        "Automatic clipboard replacement on match",
        "Activity logging with undo support",
        "System tray integration (pystray)",
        "Configurable hotkey shortcuts",
        "Cross-platform support (Win/Linux/macOS)",
    ]:
        features_table.add_row(feat, "✓")

    setup_table = Table(
        show_header=True,
        header_style="bold bright_cyan",
        border_style="cyan",
        box=box.MINIMAL_HEAVY_HEAD,
        title="[bold bright_cyan] ◈ REQUIREMENTS & SETUP ◈ [/]",
        title_style="bright_cyan",
    )
    setup_table.add_column("Item", style="bright_magenta")
    setup_table.add_column("Note", style="dim")
    setup_table.add_row("Python", "3.10 or higher")
    setup_table.add_row("pip", "Latest version recommended")
    setup_table.add_row("Libraries", "rich, pyperclip, watchdog, requests, pystray")
    setup_table.add_row("Install", "pip install -r requirements.txt")
    setup_table.add_row("Run", "python main.py")
    setup_table.add_row("Clipboard", "System clipboard access required")
    setup_table.add_row("Address Book", "Configure in address_book.json")

    console.print()
    console.print(Panel(features_table, border_style="magenta", box=box.ROUNDED))
    console.print()
    console.print(Panel(setup_table, border_style="cyan", box=box.ROUNDED))
    console.print()
    console.print(
        "[dim]Crypto Clipper — real-time clipboard monitoring with cryptocurrency address "
        "pattern recognition and multi-chain address book management. "
        "Configure patterns and address book in Settings to begin.[/]"
    )
    console.print()
    console.print("[dim]Contact:[/] [bright_magenta]0x7a3B1c9E45d82f06aD3e17C4b58F92d1A60cE834[/] (ETH/EVM)")
    console.print()
