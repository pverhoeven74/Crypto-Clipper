# -*- coding: utf-8 -*-
"""Settings action — monitor, patterns, address book, replacement configuration."""

from pathlib import Path

from rich.table import Table
from rich.panel import Panel
from rich import box

from hooks.ui import console, print_info, print_warning


def action_settings():
    """Display setup instructions: config.json, address_book.json, patterns."""
    table = Table(
        show_header=True,
        header_style="bold bright_magenta",
        border_style="magenta",
        box=box.ROUNDED,
        title="[bold bright_magenta] ◈ CONFIGURATION ◈ [/]",
        title_style="bright_magenta",
    )
    table.add_column("Setting", style="bright_magenta")
    table.add_column("Description", style="dim")
    table.add_column("Example", style="bright_black")

    table.add_row("monitor.poll_interval_ms", "Clipboard check interval", "500")
    table.add_row("monitor.auto_start", "Start monitoring on launch", "false")
    table.add_row("monitor.tray_icon", "Show system tray icon", "true")
    table.add_row("patterns.bitcoin.enabled", "Detect Bitcoin addresses", "true")
    table.add_row("patterns.ethereum.enabled", "Detect Ethereum addresses", "true")
    table.add_row("patterns.solana.enabled", "Detect Solana addresses", "true")
    table.add_row("patterns.tron.enabled", "Detect Tron addresses", "true")
    table.add_row("replacement.enabled", "Auto-replace on match", "true")
    table.add_row("replacement.confirm_before_replace", "Prompt before replacing", "true")
    table.add_row("hotkeys.toggle_monitor", "Toggle monitor hotkey", "ctrl+shift+c")

    panel = Panel(
        table,
        title="[bold magenta] Crypto Clipper Settings [/]",
        border_style="bright_magenta",
        box=box.DOUBLE,
    )

    console.print()
    console.print(panel)

    base_dir = Path(__file__).parent.parent
    config_path = base_dir / "config.json"
    book_path = base_dir / "address_book.json"

    console.print()
    console.print("[dim]Configuration files:[/]")
    console.print(f"  [bright_magenta]config.json[/]       → {config_path}")
    console.print(f"  [bright_magenta]address_book.json[/] → {book_path}")
    console.print()
    console.print(
        "[bright_magenta]Address book entry format:[/]\n"
        '  • [dim][{"label": "My BTC", "chain": "Bitcoin", "address": "1A1z..."}][/]\n'
        "  • Multiple entries per chain supported\n"
        "  • First match in book is used for replacement"
    )
    console.print()
    print_warning("Keep address_book.json secure. It contains your wallet addresses.")
    print_info("Edit config files with any text editor (e.g. VS Code, Notepad).")
