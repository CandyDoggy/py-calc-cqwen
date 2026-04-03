# How to Open Calculator

## Quick Start (Recommended)

Works on **Windows**, **macOS**, and **Linux**:

```bash
python launcher.py
```

This automatically sets up the virtual environment and installs dependencies if needed.

---

## First-Time Setup

### Step 1: Install Python

Download from: https://www.python.org/downloads/

- **Windows**: ✅ Check **"Add Python to PATH"** during install
- **macOS**: Use the installer or `brew install python3`
- **Linux**: `sudo apt install python3 python3-pip python3-venv`

### Step 2: Open the Calculator

#### Option A: Using launcher.py (Easiest)
```bash
cd calculator
python launcher.py
```

#### Option B: Manual Setup
```bash
cd calculator

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

#### Option C: Platform Scripts
- **Windows**: Double-click `run.bat`
- **macOS/Linux**: `./run.sh`

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0-9` | Enter numbers |
| `+ - * /` | Operators |
| `Enter` | Calculate |
| `Backspace` | Delete last character |
| `Escape` | Clear all |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `python: command not found` | Install Python from python.org |
| `No module named 'customtkinter'` | Run `pip install -r requirements.txt` |
| `Permission denied` (macOS/Linux) | Run `chmod +x run.sh` first |
| Windows blocks `run.bat` | Use `python launcher.py` instead |

---

## Need Help?

- See [SETUP.md](SETUP.md) for detailed setup instructions
- See [README.md](README.md) for full documentation
- Report issues: https://github.com/CandyDoggy/py-calc-cqwen/issues
