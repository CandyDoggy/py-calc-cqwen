#!/usr/bin/env python3
"""
Scientific Calculator with Modern UI

A powerful calculator application featuring:
- Basic arithmetic operations
- Scientific functions (trig, log, exp)
- Symbolic math capabilities
- Modern dark/light theme
- Calculation history

Run with: python main.py
"""

import sys
import os

# Add the project root to the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.calculator_ui import run_calculator


def main():
    """Main entry point for the calculator application."""
    print("Starting Scientific Calculator...")
    print("Press Ctrl+C to exit.\n")
    
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
