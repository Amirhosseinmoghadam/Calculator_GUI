import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ماشین حساب")
        self.geometry("400x600")
        self.configure(bg="black")
        self.resizable(True, True)

        self.expression = ""
        self.create_widgets()
        self.bind("<Key>", self.handle_keypress)

    def create_widgets(self):
        # Entry field
        self.entry = ttk.Entry(
            self,
            font=("Arial", 24),
            justify="right",
            state="readonly",
        )
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Buttons layout
        buttons = [
            ('%', 1, 0, "dark gray"), ('CE', 1, 1, "dark gray"), ('C', 1, 2, "dark gray"), ('⌫', 1, 3, "dark gray"),
            ('1/x', 2, 0, "dark gray"), ('x²', 2, 1, "dark gray"), ('√x', 2, 2, "dark gray"), ('÷', 2, 3, "dark gray"),
            ('7', 3, 0, "dark gray"), ('8', 3, 1, "dark gray"), ('9', 3, 2, "dark gray"), ('×', 3, 3, "dark gray"),
            ('4', 4, 0, "dark gray"), ('5', 4, 1, "dark gray"), ('6', 4, 2, "dark gray"), ('-', 4, 3, "dark gray"),
            ('1', 5, 0, "dark gray"), ('2', 5, 1, "dark gray"), ('3', 5, 2, "dark gray"), ('+', 5, 3, "dark gray"),
            ('+/-', 6, 0, "dark gray"), ('0', 6, 1, "dark gray"), ('.', 6, 2, "dark gray"), ('=', 6, 3, "dark gray")
        ]

        for text, row, col, color in buttons:
            btn = ttk.Button(
                self, text=text, command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew")

        # Row and column weights for responsiveness
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        # Custom styles
        style = ttk.Style(self)
        style.configure("TButton", font=("Arial", 20), padding=10)

    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char in {"C", "CE"}:
            self.expression = ""
            self.update_entry()
        elif char == "⌫":
            self.expression = self.expression[:-1]
            self.update_entry()

        elif char == "+/-":
            if self.expression:
                if self.expression.lstrip('-').isdigit():  # Check if it's an integer
                    self.expression = str(-int(self.expression))
                elif self.expression.lstrip('-').replace('.', '', 1).isdigit():  # Check if it's a float
                    self.expression = str(-float(self.expression))
                self.update_entry()
        elif char == "1/x":
            try:
                self.expression = str(1 / float(self.expression))
                self.update_entry()
            except Exception:
                self.expression = "خطا"
                self.update_entry()

        elif char == "x²":
            try:
                result = float(self.expression) ** 2
                self.expression = str(int(result)) if result.is_integer() else str(result)
                self.update_entry()
            except Exception:
                self.expression = "خطا"
                self.update_entry()
        elif char == "√x":
            try:
                self.expression = str(float(self.expression) ** 0.5)
                self.update_entry()
            except Exception:
                self.expression = "خطا"
                self.update_entry()
        elif char == "%":
            try:
                self.expression = str(float(self.expression) / 100)
                self.update_entry()
            except Exception:
                self.expression = "خطا"
                self.update_entry()
        else:
            self.expression += char
            self.update_entry()

    def calculate(self):
        try:
            self.expression = str(eval(self.expression.replace('×', '*').replace('÷', '/')))
        except Exception:
            self.expression = "خطا"
        self.update_entry()

    def update_entry(self):
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)
        self.entry.config(state="readonly")

    def handle_keypress(self, event):
        key = event.char
        if key in "0123456789.+-*/":
            self.on_button_click(key)
        elif key == "\r":  # Enter key
            self.on_button_click("=")
        elif key == "\x08":  # Backspace key
            self.on_button_click("⌫")
        elif event.keysym == "Escape":  # Esc key
            self.on_button_click("CE")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()



