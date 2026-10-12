# -*- coding: utf-8 -*-
"""Clipboard injector — replaces clipboard content with address book entry."""

import time
from typing import Optional


def inject_address(address: str, original: str) -> dict:
    """Replace clipboard content with target address.

    Returns operation record with timestamps and metadata.
    """
    record = {
        "timestamp": time.time(),
        "original_preview": original[:32] + "..." if len(original) > 32 else original,
        "replacement": address,
        "status": "pending",
    }

    try:
        import pyperclip
        pyperclip.copy(address)
        record["status"] = "success"
    except ImportError:
        record["status"] = "error"
        record["error"] = "pyperclip not installed"
    except Exception as e:
        record["status"] = "error"
        record["error"] = str(e)

    return record


def undo_inject(original: str) -> bool:
    """Restore original clipboard content."""
    try:
        import pyperclip
        pyperclip.copy(original)
        return True
    except Exception:
        return False


def get_clipboard() -> Optional[str]:
    """Read current clipboard content."""
    try:
        import pyperclip
        return pyperclip.paste()
    except Exception:
        return None
