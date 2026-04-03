#!/bin/bash
# Scientific Calculator Launcher
# Works on macOS and Linux

set -e

echo "========================================"
echo "  Scientific Calculator Launcher"
echo "========================================"
echo ""

# Detect OS
OS="$(uname -s)"

# Check if Python 3 is installed
if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "ERROR: Python 3 is not installed."
    echo "Download Python from: https://www.python.org/downloads/"
    exit 1
fi

echo "Using Python: $($PYTHON --version)"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Setting up virtual environment..."
    $PYTHON -m venv venv

    # Activate and install dependencies
    if [ "$OS" = "Darwin" ] || [ "$OS" = "Linux" ]; then
        source venv/bin/activate
    fi

    pip install -r requirements.txt
    echo ""
fi

echo "Starting Calculator..."
echo ""

# Run with venv Python
if [ "$OS" = "Darwin" ] || [ "$OS" = "Linux" ]; then
    venv/bin/python main.py
else
    venv/Scripts/python.exe main.py
fi
