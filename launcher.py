#!/usr/bin/env python3
"""
Cross-platform launcher for Calculator.
Works on Windows, macOS, and Linux.
Automatically sets up virtual environment if needed.
"""

import os
import sys
import subprocess
import platform


def get_venv_python():
    """Get the path to the virtual environment's Python executable."""
    system = platform.system()
    if system == "Windows":
        return os.path.join("venv", "Scripts", "python.exe")
    else:
        return os.path.join("venv", "bin", "python")


def get_pip_path():
    """Get the path to pip in the virtual environment."""
    system = platform.system()
    if system == "Windows":
        return os.path.join("venv", "Scripts", "pip.exe")
    else:
        return os.path.join("venv", "bin", "pip")


def run_command(cmd, description=""):
    """Run a command and print output."""
    if description:
        print(f"  {description}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERROR: {result.stderr.strip()}")
        return False
    return True


def setup_venv():
    """Create virtual environment and install dependencies."""
    print("Setting up virtual environment...")

    if not run_command([sys.executable, "-m", "venv", "venv"], "Creating venv"):
        print("\nFailed to create virtual environment.")
        print("Make sure you have python3-venv installed:")
        print("  Ubuntu/Debian: sudo apt install python3-venv")
        return False

    print()

    pip_path = get_pip_path()
    requirements = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")

    if not run_command([pip_path, "install", "-r", requirements], "Installing dependencies"):
        print("\nFailed to install dependencies.")
        print("Try manually: pip install -r requirements.txt")
        return False

    print()
    return True


def main():
    """Main launcher logic."""
    system = platform.system()
    print("=" * 40)
    print("  Calculator Launcher")
    print(f"  Platform: {system}")
    print("=" * 40)
    print()

    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    venv_python = get_venv_python()

    # Check if venv exists
    if not os.path.exists(venv_python):
        if not setup_venv():
            input("\nPress Enter to exit...")
            sys.exit(1)
        print("Setup complete!")
        print()

    # Run the calculator
    print("Starting Calculator...")
    print()
    main_py = os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py")
    subprocess.run([venv_python, main_py])


if __name__ == "__main__":
    main()
