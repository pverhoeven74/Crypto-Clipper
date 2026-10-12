# -*- coding: utf-8 -*-
"""Address filter — chain-specific filtering and address book matching."""

import json
from pathlib import Path
from typing import Optional


class AddressFilter:
    """Filters detected addresses by chain and matches against address book."""

    def __init__(self, config: dict):
        self._config = config
        self._patterns = config.get("patterns", {})
        self._book: list[dict] = []
        self._load_book()

    def _load_book(self):
        """Load address book from file."""
        book_cfg = self._config.get("address_book", {})
        book_file = book_cfg.get("file", "address_book.json")
        book_path = Path(__file__).parent.parent / book_file
        if book_path.exists():
            try:
                with open(book_path, "r", encoding="utf-8") as f:
                    self._book = json.load(f)
            except (json.JSONDecodeError, OSError):
                self._book = []

    def is_chain_enabled(self, chain: str) -> bool:
        """Check if a chain's pattern detection is enabled."""
        chain_cfg = self._patterns.get(chain.lower(), {})
        if isinstance(chain_cfg, dict):
            return chain_cfg.get("enabled", False)
        return False

    def find_book_match(self, address: str) -> Optional[dict]:
        """Find matching entry in address book."""
        for entry in self._book:
            if entry.get("address", "").lower() == address.lower():
                return entry
        return None

    def get_replacement(self, detected_chain: str) -> Optional[str]:
        """Get replacement address for a detected chain from address book."""
        for entry in self._book:
            if entry.get("chain", "").lower() == detected_chain.lower():
                return entry.get("address")
        return None

    @property
    def book_size(self) -> int:
        return len(self._book)
