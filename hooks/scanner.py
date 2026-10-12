# -*- coding: utf-8 -*-
"""Address pattern scanner — regex-based crypto address detection engine."""

import re
from typing import Optional

# Bitcoin patterns
BTC_LEGACY = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')
BTC_SEGWIT = re.compile(r'^bc1[a-z0-9]{39,59}$')
BTC_TAPROOT = re.compile(r'^bc1p[a-z0-9]{58}$')

# Ethereum pattern (0x + 40 hex chars)
ETH_PATTERN = re.compile(r'^0x[0-9a-fA-F]{40}$')

# Solana pattern (32-44 base58 chars)
SOL_PATTERN = re.compile(r'^[1-9A-HJ-NP-Za-km-z]{32,44}$')

# Tron pattern (T + 33 base58 chars)
TRX_PATTERN = re.compile(r'^T[1-9A-HJ-NP-Za-km-z]{33}$')

# Litecoin patterns
LTC_LEGACY = re.compile(r'^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$')
LTC_SEGWIT = re.compile(r'^ltc1[a-z0-9]{39,59}$')

# Dogecoin pattern
DOGE_PATTERN = re.compile(r'^D[1-9A-HJ-NP-Za-km-z]{25,34}$')


def detect_address(text: str) -> Optional[dict]:
    """Detect cryptocurrency address in clipboard text.

    Returns dict with 'chain', 'address', 'format' keys or None.
    """
    text = text.strip()

    if BTC_TAPROOT.match(text):
        return {"chain": "Bitcoin", "address": text, "format": "Taproot (bc1p)"}
    if BTC_SEGWIT.match(text):
        return {"chain": "Bitcoin", "address": text, "format": "SegWit (bc1)"}
    if BTC_LEGACY.match(text):
        return {"chain": "Bitcoin", "address": text, "format": "Legacy (1/3)"}
    if ETH_PATTERN.match(text):
        return {"chain": "Ethereum", "address": text, "format": "EVM (0x)"}
    if TRX_PATTERN.match(text):
        return {"chain": "Tron", "address": text, "format": "Base58 (T)"}
    if LTC_SEGWIT.match(text):
        return {"chain": "Litecoin", "address": text, "format": "SegWit (ltc1)"}
    if LTC_LEGACY.match(text):
        return {"chain": "Litecoin", "address": text, "format": "Legacy (L/M)"}
    if DOGE_PATTERN.match(text):
        return {"chain": "Dogecoin", "address": text, "format": "Legacy (D)"}
    if SOL_PATTERN.match(text):
        return {"chain": "Solana", "address": text, "format": "Base58"}

    return None


def validate_checksum(address: str, chain: str) -> bool:
    """Validate address checksum where applicable (EIP-55 for ETH)."""
    if chain == "Ethereum":
        if address == address.lower() or address == address.upper():
            return True
        try:
            from hashlib import sha3_256
            addr_lower = address[2:].lower()
            hash_hex = sha3_256(addr_lower.encode()).hexdigest()
            for i, c in enumerate(address[2:]):
                if c.isalpha():
                    if int(hash_hex[i], 16) >= 8:
                        if not c.isupper():
                            return False
                    else:
                        if not c.islower():
                            return False
            return True
        except Exception:
            return True
    return True
