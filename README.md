# Scientific Calculator

A modern, feature-rich calculator application built with Python and CustomTkinter.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division
- **Scientific Functions**: sin, cos, tan, log, ln, sqrt, exp
- **Advanced Math**: Powers, roots, percentages, negation
- **Constants**: π (pi), e (Euler's number)
- **Calculation History**: View and manage past calculations
- **Modern UI**: Dark theme with CustomTkinter
- **Error Handling**: Clear error messages for invalid expressions

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Launch the Calculator

```bash
python main.py
```

### Keyboard Support

- **Enter**: Calculate result
- **Backspace**: Delete last character
- **Numbers (0-9)**: Input numbers
- **Operators (+, -, *, /)**: Basic operations
- **Escape**: Clear all (C)

## Project Structure

```
calculator/
├── main.py              # Entry point
├── ui/
│   ├── __init__.py
│   └── calculator_ui.py # UI components (CustomTkinter)
├── math_engine/
│   ├── __init__.py
│   └── calculator.py    # Math logic (SymPy, NumPy)
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── PLAN.md             # Development plan
```

## Supported Operations

| Category | Operations |
|----------|------------|
| Basic | +, -, ×, ÷ |
| Scientific | sin, cos, tan, asin, acos, atan |
| Logarithmic | log (base 10), ln (natural log) |
| Powers | x², xʸ, √ (square root) |
| Constants | π, e |
| Other | %, 1/x, ± (negation) |

## Examples

| Expression | Result |
|------------|--------|
| `2 + 3 * 4` | 14 |
| `sin(pi/2)` | 1.0 |
| `sqrt(16)` | 4.0 |
| `log(100)` | 2.0 |
| `2 ** 10` | 1024 |
| `(5 + 3) * 2` | 16 |

## Dependencies

- **customtkinter** - Modern UI framework
- **sympy** - Symbolic mathematics
- **numpy** - Numerical computing
- **scipy** - Scientific computing

## Troubleshooting

### Common Issues

**"No module named 'customtkinter'"**
```bash
pip install customtkinter
```

**Display issues on Linux**
```bash
# Ensure you have a display server running
# For Wayland users, try running with X11:
GDK_BACKEND=x11 python main.py
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## Author

Created as a demonstration of Python GUI development with CustomTkinter and SymPy.
