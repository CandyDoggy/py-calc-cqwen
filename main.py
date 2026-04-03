#!/usr/bin/env python3
"""
Scientific Calculator with Modern UI

A powerful calculator application featuring:
- Basic arithmetic operations
- Scientific functions (trig, log, exp)
- Symbolic math capabilities
- Modern dark/light theme
- Calculation history

Cross-platform: Windows, macOS, Linux

Run with:
  Windows:  python main.py  or  run.bat
  macOS:    python3 main.py  or  ./run.sh
  Linux:    python3 main.py  or  ./run.sh
"""

import sys
import os
import platform

# Add the project root to the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def check_dependencies():
    """Check if required dependencies are installed."""
    missing = []
    try:
        import customtkinter
    except ImportError:
        missing.append("customtkinter")
    try:
        import sympy
    except ImportError:
        missing.append("sympy")
    try:
        import numpy
    except ImportError:
        missing.append("numpy")

    if missing:
        print("=" * 50)
        print("Missing dependencies:")
        for pkg in missing:
            print(f"  - {pkg}")
        print("=" * 50)
        print(f"\nTo install, run:")
        print(f"  pip install -r requirements.txt")
        print(f"\nOr install individually:")
        for pkg in missing:
            print(f"  pip install {pkg}")
        print()
        return False
    return True


def main():
    """Main entry point for the calculator application."""
    os_name = platform.system()
    print(f"Starting Scientific Calculator ({os_name})...")
    print("Press Ctrl+C to exit.\n")

    if not check_dependencies():
        sys.exit(1)

    from ui.calculator_ui import run_calculator

    try:
        run_calculator()
    except KeyboardInterrupt:
        print("\nCalculator closed.")
        sys.exit(0)
    except Exception as e:
        print(f"Error starting calculator: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
