"""
UI module for the calculator using CustomTkinter.
Supports multiple modes: Minimalistic, Scientific, Programmer, and Modern.
"""

import customtkinter as ctk
from typing import Callable, Dict, List
from math_engine.calculator import Calculator, CalculatorError


class CalculatorUI(ctk.CTk):
    """Main calculator UI window with multiple modes."""
    
    # Mode configurations
    MODES = {
        "minimalistic": {
            "name": "Minimalistic",
            "buttons": [
                ("7", "number"), ("8", "number"), ("9", "number"), ("÷", "operator"),
                ("4", "number"), ("5", "number"), ("6", "number"), ("×", "operator"),
                ("1", "number"), ("2", "number"), ("3", "number"), ("-", "operator"),
                ("0", "number"), (".", "number"), ("=", "action"), ("+", "operator"),
                ("C", "action"), ("⌫", "action"),
            ],
            "colors": {
                "bg": "#1a1a1a",
                "frame": "#2d2d2d",
                "operator": "#ff9500",
                "action": "#ff6b35",
                "number": "#333333",
                "text": "#ffffff",
            },
            "geometry": "320x480",
            "btn_height": 60,
        },
        "scientific": {
            "name": "Scientific",
            "buttons": [
                ("sin", "sci"), ("cos", "sci"), ("tan", "sci"), ("log", "sci"), ("ln", "sci"),
                ("√", "sci"), ("x²", "sci"), ("xʸ", "sci"), ("(", "operator"), (")", "operator"),
                ("7", "number"), ("8", "number"), ("9", "number"), ("÷", "operator"), ("C", "action"),
                ("4", "number"), ("5", "number"), ("6", "number"), ("×", "operator"), ("⌫", "action"),
                ("1", "number"), ("2", "number"), ("3", "number"), ("-", "operator"), ("=", "action"),
                ("0", "number"), (".", "number"), ("π", "sci"), ("+", "operator"), ("±", "action"),
                ("e", "sci"), ("exp", "sci"), ("1/x", "sci"), ("%", "operator"), ("History", "action"),
            ],
            "colors": {
                "bg": "#1e1e1e",
                "frame": "#252525",
                "operator": "#0078d4",
                "action": "#d84315",
                "number": "#3a3a3a",
                "sci": "#008751",
                "text": "#ffffff",
            },
            "geometry": "480x620",
            "btn_height": 55,
        },
        "programmer": {
            "name": "Programmer",
            "buttons": [
                ("Hex", "prog"), ("Dec", "prog"), ("Oct", "prog"), ("Bin", "prog"),
                ("AND", "prog"), ("OR", "prog"), ("XOR", "prog"), ("NOT", "prog"),
                ("7", "number"), ("8", "number"), ("9", "number"), ("÷", "operator"), ("C", "action"),
                ("4", "number"), ("5", "number"), ("6", "number"), ("×", "operator"), ("⌫", "action"),
                ("1", "number"), ("2", "number"), ("3", "number"), ("-", "operator"), ("=", "action"),
                ("0", "number"), (".", "number"), ("A", "prog"), ("B", "prog"), ("+", "operator"),
                ("C", "prog"), ("D", "prog"), ("E", "prog"), ("F", "prog"), ("MOD", "prog"), ("±", "action"),
            ],
            "colors": {
                "bg": "#1a1a2e",
                "frame": "#16213e",
                "operator": "#0f3460",
                "action": "#e94560",
                "number": "#2d2d44",
                "prog": "#7c3aed",
                "text": "#ffffff",
            },
            "geometry": "480x680",
            "btn_height": 50,
        },
        "modern": {
            "name": "Modern",
            "buttons": [
                ("sin", "sci"), ("cos", "sci"), ("tan", "sci"), ("C", "action"),
                ("√", "sci"), ("x²", "sci"), ("xʸ", "sci"), ("⌫", "action"),
                ("7", "number"), ("8", "number"), ("9", "number"), ("÷", "operator"),
                ("4", "number"), ("5", "number"), ("6", "number"), ("×", "operator"),
                ("1", "number"), ("2", "number"), ("3", "number"), ("-", "operator"),
                ("0", "number"), (".", "number"), ("=", "action"), ("+", "operator"),
            ],
            "colors": {
                "bg": "#0f0f0f",
                "frame": "#1a1a1a",
                "operator": "#bb86fc",
                "action": "#03dac6",
                "number": "#2c2c2c",
                "sci": "#cf6679",
                "text": "#ffffff",
            },
            "geometry": "380x550",
            "btn_height": 58,
        },
    }
    
    def __init__(self):
        super().__init__()
        
        self.calculator = Calculator()
        self.current_mode = "scientific"  # Default mode
        self.base_mode = "dec"  # For programmer mode: dec, hex, oct, bin
        
        # Configure window
        self.title("Scientific Calculator")
        self.geometry(self.MODES[self.current_mode]["geometry"])
        self.resizable(True, True)
        self.minsize(300, 400)
        
        # Set appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Configure main grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Mode selector
        self.grid_rowconfigure(1, weight=0)  # Display
        self.grid_rowconfigure(2, weight=1)  # Buttons
        
        # Create UI components
        self._create_mode_selector()
        self._create_display_frame()
        self._create_buttons_frame()
        
    def _create_mode_selector(self):
        """Create mode selector bar."""
        self.mode_frame = ctk.CTkFrame(self, corner_radius=10, height=45)
        self.mode_frame.grid(row=0, column=0, sticky="ew", padx=15, pady=10)
        self.mode_frame.grid_columnconfigure(0, weight=1)
        
        # Center the mode buttons
        center_frame = ctk.CTkFrame(self.mode_frame, fg_color="transparent")
        center_frame.grid(row=0, column=0, sticky="ew", padx=10)
        
        # Mode selector buttons
        self.mode_buttons = {}
        modes = list(self.MODES.keys())
        for i, mode_key in enumerate(modes):
            mode_name = self.MODES[mode_key]["name"]
            btn = ctk.CTkButton(
                center_frame,
                text=mode_name,
                width=95,
                height=32,
                corner_radius=8,
                font=ctk.CTkFont(size=12, weight="bold"),
                command=lambda m=mode_key: self._switch_mode(m),
            )
            btn.grid(row=0, column=i, padx=4, pady=6)
            self.mode_buttons[mode_key] = btn
        
        self._update_mode_buttons()
        
    def _switch_mode(self, mode: str):
        """Switch calculator mode."""
        self.current_mode = mode
        self.geometry(self.MODES[mode]["geometry"])
        self._update_mode_buttons()
        self._recreate_buttons()
        
    def _update_mode_buttons(self):
        """Update mode button colors."""
        colors = self.MODES[self.current_mode]["colors"]
        for mode_key, btn in self.mode_buttons.items():
            if mode_key == self.current_mode:
                btn.configure(fg_color=colors["action"], hover_color=colors["action"])
            else:
                btn.configure(fg_color=colors["operator"], hover_color=colors["frame"])
        
    def _create_display_frame(self):
        """Create the display frame with entry and history."""
        self.display_frame = ctk.CTkFrame(self, corner_radius=15)
        self.display_frame.grid(row=1, column=0, sticky="ew", padx=15, pady=10)
        self.display_frame.grid_columnconfigure(0, weight=1)
        
        # Top bar with mode and base indicator
        top_bar = ctk.CTkFrame(self.display_frame, fg_color="transparent", height=30)
        top_bar.grid(row=0, column=0, sticky="ew", padx=15, pady=(15, 5))
        top_bar.grid_columnconfigure(0, weight=1)
        
        # Mode indicator
        self.mode_indicator_var = ctk.StringVar(value="Scientific")
        self.mode_indicator = ctk.CTkLabel(
            top_bar,
            textvariable=self.mode_indicator_var,
            font=ctk.CTkFont(size=13, weight="bold"),
            anchor="w",
            text_color="#888888"
        )
        self.mode_indicator.grid(row=0, column=0, sticky="w")
        
        # Base indicator (for programmer mode)
        self.base_indicator_var = ctk.StringVar(value="DEC")
        self.base_indicator = ctk.CTkLabel(
            top_bar,
            textvariable=self.base_indicator_var,
            font=ctk.CTkFont(size=11, weight="bold"),
            anchor="e",
            height=25,
            text_color="#0078d4",
            corner_radius=5
        )
        self.base_indicator.grid(row=0, column=0, sticky="e", padx=10)
        
        # Expression display
        self.expression_var = ctk.StringVar(value="")
        self.expression_label = ctk.CTkLabel(
            self.display_frame,
            textvariable=self.expression_var,
            font=ctk.CTkFont(size=16),
            anchor="e",
            height=35,
            text_color="#888888"
        )
        self.expression_label.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 5))
        
        # Result display
        self.result_var = ctk.StringVar(value="0")
        self.result_entry = ctk.CTkLabel(
            self.display_frame,
            textvariable=self.result_var,
            font=ctk.CTkFont(size=42, weight="bold"),
            anchor="e",
            height=70,
            text_color="#ffffff"
        )
        self.result_entry.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 15))
        
        # Bind keyboard events
        self.bind("<Return>", lambda e: self._calculate())
        self.bind("<Escape>", lambda e: self._on_action("C"))
        self.bind("<BackSpace>", lambda e: self._on_action("⌫"))
        
    def _create_buttons_frame(self):
        """Create the buttons frame."""
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.grid(row=2, column=0, sticky="nsew", padx=15, pady=(0, 15))
        self._recreate_buttons()
        
    def _recreate_buttons(self):
        """Recreate buttons based on current mode."""
        # Clear existing buttons
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        
        mode_config = self.MODES[self.current_mode]
        buttons = mode_config["buttons"]
        colors = mode_config["colors"]
        btn_height = mode_config.get("btn_height", 55)
        
        # Calculate grid size
        num_cols = 4
        if len(buttons) > 20:
            num_cols = 5
        
        # Configure grid weights for uniform button sizing
        for i in range(num_cols):
            self.buttons_frame.grid_columnconfigure(i, weight=1, uniform="btn")
        num_rows = (len(buttons) + num_cols - 1) // num_cols
        for i in range(num_rows):
            self.buttons_frame.grid_rowconfigure(i, weight=1, uniform="btn")
        
        # Create buttons
        self.buttons = {}
        for idx, (text, btn_type) in enumerate(buttons):
            row = idx // num_cols
            col = idx % num_cols
            
            btn = self._create_button(text, btn_type, colors, btn_height)
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)
            self.buttons[text] = btn
            
        # Update mode indicator
        self.mode_indicator_var.set(mode_config['name'])
        
    def _create_button(self, text: str, command_type: str, colors: Dict, height: int) -> ctk.CTkButton:
        """Create a calculator button with mode-specific colors."""
        
        color_map = {
            "number": (colors["number"], colors["text"]),
            "operator": (colors["operator"], colors["text"]),
            "action": (colors["action"], colors["text"]),
            "sci": (colors.get("sci", colors["operator"]), colors["text"]),
            "prog": (colors.get("prog", colors["operator"]), colors["text"]),
        }
        
        fg_color, text_color = color_map.get(command_type, (colors["number"], colors["text"]))
        
        # Determine font size based on button type and text length
        if command_type == "number":
            font_size = 24
            font_weight = "bold"
        elif len(text) > 3:
            font_size = 13
            font_weight = "bold"
        else:
            font_size = 18
            font_weight = "bold"
        
        btn = ctk.CTkButton(
            self.buttons_frame,
            text=text,
            font=ctk.CTkFont(size=font_size, weight=font_weight),
            command=lambda t=text, ct=command_type: self._on_button(t, ct),
            fg_color=fg_color,
            hover_color=self._lighten_color(fg_color),
            text_color=text_color,
            corner_radius=12,
            height=height,
        )
        
        return btn
    
    def _lighten_color(self, color: str) -> str:
        """Lighten a hex color slightly for hover effect."""
        try:
            color = color.lstrip('#')
            r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
            factor = 1.15
            r = min(255, int(r * factor))
            g = min(255, int(g * factor))
            b = min(255, int(b * factor))
            return f"#{r:02x}{g:02x}{b:02x}"
        except:
            return color
    
    def _on_button(self, text: str, cmd_type: str):
        """Handle button press based on type."""
        if cmd_type == "number":
            self._on_number(text)
        elif cmd_type == "operator":
            self._on_operator(text)
        elif cmd_type == "action":
            self._on_action(text)
        elif cmd_type == "sci":
            self._on_scientific(text)
        elif cmd_type == "prog":
            self._on_programmer(text)
    
    def _on_number(self, num: str):
        """Handle number button press."""
        current = self.result_var.get()
        if current == "0" or current == "Error":
            self.result_var.set(num)
        else:
            self.result_var.set(current + num)
    
    def _on_operator(self, op: str):
        """Handle operator button press."""
        current = self.result_var.get()
        if current == "Error":
            self.result_var.set("")
            self.expression_var.set("")
            return
        
        # Convert display operators to Python operators
        op_map = {"×": "*", "÷": "/", "x²": "**2", "xʸ": "**"}
        py_op = op_map.get(op, op)
        
        self.expression_var.set(current + " " + py_op)
        self.result_var.set("0")
    
    def _on_scientific(self, func: str):
        """Handle scientific function button press."""
        current = self.result_var.get()
        
        func_map = {
            "sin": "sin(",
            "cos": "cos(",
            "tan": "tan(",
            "log": "log(",
            "ln": "ln(",
            "√": "sqrt(",
            "x²": "**2",
            "xʸ": "**",
            "π": "pi",
            "e": "e",
            "exp": "exp(",
            "1/x": "1/(",
        }
        
        py_func = func_map.get(func, func)
        
        if func in ["π", "e"]:
            if current == "0" or current == "Error":
                self.result_var.set(py_func)
            else:
                self.result_var.set(current + py_func)
        elif func == "x²":
            self.expression_var.set(current + "**2")
            self.result_var.set("0")
        elif func == "1/x":
            self.expression_var.set("1/(" + current + ")")
            self.result_var.set("0")
        else:
            if current == "0" or current == "Error":
                self.result_var.set(py_func)
            else:
                self.result_var.set(current + py_func)
    
    def _on_programmer(self, func: str):
        """Handle programmer mode button press."""
        current = self.result_var.get()
        
        if func == "Hex":
            self.base_mode = "hex"
            self.base_indicator_var.set("HEX")
        elif func == "Dec":
            self.base_mode = "dec"
            self.base_indicator_var.set("DEC")
        elif func == "Oct":
            self.base_mode = "oct"
            self.base_indicator_var.set("OCT")
        elif func == "Bin":
            self.base_mode = "bin"
            self.base_indicator_var.set("BIN")
        elif func == "Base":
            self._convert_base()
            return
        elif func in ["A", "B", "C", "D", "E", "F"]:
            if self.base_mode == "hex":
                if current == "0" or current == "Error":
                    self.result_var.set(func)
                else:
                    self.result_var.set(current + func)
                return
        elif func == "AND":
            self.expression_var.set(current + " & ")
            self.result_var.set("0")
            return
        elif func == "OR":
            self.expression_var.set(current + " | ")
            self.result_var.set("0")
            return
        elif func == "XOR":
            self.expression_var.set(current + " ^ ")
            self.result_var.set("0")
            return
        elif func == "NOT":
            try:
                val = int(current)
                self.result_var.set(str(~val))
            except ValueError:
                self.result_var.set("Error")
            return
        elif func == "MOD":
            self.expression_var.set(current + " % ")
            self.result_var.set("0")
            return
        
        self._on_number(func) if func not in ["AND", "OR", "XOR", "NOT", "MOD"] else None
    
    def _convert_base(self):
        """Convert current result to selected base."""
        try:
            current = self.result_var.get()
            if current == "Error":
                return
            val = int(float(current))
            
            if self.base_mode == "hex":
                self.result_var.set(hex(val)[2:].upper())
            elif self.base_mode == "oct":
                self.result_var.set(oct(val)[2:])
            elif self.base_mode == "bin":
                self.result_var.set(bin(val)[2:])
            elif self.base_mode == "dec":
                self.result_var.set(str(val))
        except ValueError:
            self.result_var.set("Error")
    
    def _on_action(self, action: str):
        """Handle action button press."""
        if action == "C":
            self.result_var.set("0")
            self.expression_var.set("")
        elif action == "⌫":
            current = self.result_var.get()
            if current == "Error" or len(current) <= 1:
                self.result_var.set("0")
            else:
                self.result_var.set(current[:-1])
        elif action == "=":
            self._calculate()
        elif action == "±":
            current = self.result_var.get()
            if current != "0" and current != "Error":
                if current.startswith("-"):
                    self.result_var.set(current[1:])
                else:
                    self.result_var.set("-" + current)
        elif action == "History":
            self._show_history()
    
    def _calculate(self):
        """Perform the calculation."""
        expression = self.expression_var.get() + self.result_var.get()
        
        try:
            result = self.calculator.evaluate(expression)
            self.result_var.set(result)
            self.expression_var.set("")
        except CalculatorError as e:
            self.result_var.set("Error")
            self.expression_var.set(str(e))
    
    def _show_history(self):
        """Show calculation history in a new window."""
        history_window = ctk.CTkToplevel(self)
        history_window.title("History")
        history_window.geometry("400x400")
        history_window.attributes('-topmost', True)
        
        # Style the history window
        colors = self.MODES[self.current_mode]["colors"]
        history_window.configure(bg=colors["bg"])
        
        history_label = ctk.CTkLabel(
            history_window,
            text="Calculation History",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        history_label.pack(pady=15)
        
        history_text = ctk.CTkTextbox(history_window, width=360, height=280, corner_radius=10)
        history_text.pack(pady=10, padx=20)
        
        history = self.calculator.get_history()
        if history:
            for expr, result in reversed(history):
                history_text.insert("end", f"{expr} = {result}\n")
        else:
            history_text.insert("end", "No history yet")
        
        history_text.configure(state="disabled")
        
        btn_frame = ctk.CTkFrame(history_window, fg_color="transparent")
        btn_frame.pack(pady=10)
        
        clear_btn = ctk.CTkButton(
            btn_frame,
            text="Clear History",
            command=lambda: [self.calculator.clear_history(), history_window.destroy()],
            fg_color=colors["action"],
            width=120,
            height=35,
            corner_radius=8
        )
        clear_btn.pack(side="left", padx=10)
        
        close_btn = ctk.CTkButton(
            btn_frame,
            text="Close",
            command=history_window.destroy,
            fg_color=colors["operator"],
            width=100,
            height=35,
            corner_radius=8
        )
        close_btn.pack(side="left", padx=10)


def run_calculator():
    """Run the calculator application."""
    app = CalculatorUI()
    app.mainloop()


if __name__ == "__main__":
    run_calculator()
