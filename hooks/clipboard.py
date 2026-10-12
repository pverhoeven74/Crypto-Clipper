# -*- coding: utf-8 -*-
"""Clipboard monitor — polling-based clipboard watcher with change detection."""

import time
import threading
from typing import Callable, Optional


class ClipboardMonitor:
    """Polling-based clipboard monitor with change callback."""

    def __init__(self, poll_interval_ms: int = 500):
        self._interval = poll_interval_ms / 1000.0
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._last_content: Optional[str] = None
        self._callbacks: list[Callable] = []
        self._lock = threading.Lock()

    def on_change(self, callback: Callable):
        """Register a callback for clipboard changes."""
        self._callbacks.append(callback)

    def start(self):
        """Start monitoring clipboard."""
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._poll_loop, daemon=True)
        self._thread.start()

    def stop(self):
        """Stop monitoring clipboard."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=2.0)
            self._thread = None

    @property
    def is_running(self) -> bool:
        return self._running

    def _poll_loop(self):
        try:
            import pyperclip
        except ImportError:
            return

        while self._running:
            try:
                content = pyperclip.paste()
                with self._lock:
                    if content != self._last_content:
                        self._last_content = content
                        for cb in self._callbacks:
                            try:
                                cb(content)
                            except Exception:
                                pass
            except Exception:
                pass
            time.sleep(self._interval)
