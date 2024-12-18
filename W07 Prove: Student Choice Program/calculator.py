import math
import tkinter as tk
from tkinter import ttk, messagebox

# Standalone functions for basic and advanced operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def calculate_sine(value):
    return math.sin(math.radians(value))

def calculate_cosine(value):
    return math.cos(math.radians(value))

def calculate_logarithm(value):
    if value <= 0:
        raise ValueError("Logarithm base must be greater than 0.")
    return math.log(value)


# Class for the calculator GUI
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.create_widgets()

    def create_widgets(self):
        # Input fields
        self.num1_label = ttk.Label(self.root, text="Number 1:")
        self.num1_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.num1_entry = ttk.Entry(self.root, width=15)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        self.num2_label = ttk.Label(self.root, text="Number 2:")
        self.num2_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.num2_entry = ttk.Entry(self.root, width=15)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        # Operation selection
        self.operation_label = ttk.Label(self.root, text="Operation:")
        self.operation_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.operation_var = tk.StringVar()
        self.operation_dropdown = ttk.Combobox(
            self.root,
            textvariable=self.operation_var,
            values=["Add", "Subtract", "Multiply", "Divide", "Sine", "Cosine", "Logarithm"],
            state="readonly",
        )
        self.operation_dropdown.grid(row=2, column=1, padx=5, pady=5)
        self.operation_dropdown.current(0)

        # Result display
        self.result_label = ttk.Label(self.root, text="Result:")
        self.result_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.result_value = ttk.Label(self.root, text="", relief="sunken", anchor="center", width=20)
        self.result_value.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        self.calculate_button = ttk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.clear_button = ttk.Button(self.root, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Status bar
        self.status_bar = ttk.Label(self.root, text="Ready", relief="sunken", anchor="w")
        self.status_bar.grid(row=6, column=0, columnspan=2, sticky="we", pady=(10, 0))

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            operation = self.operation_var.get()

            if operation in ["Add", "Subtract", "Multiply", "Divide"] and not self.num2_entry.get():
                raise ValueError("Number 2 is required for basic operations.")
            
            num2 = float(self.num2_entry.get()) if self.num2_entry.get() else None

            if operation == "Add":
                result = add(num1, num2)
            elif operation == "Subtract":
                result = subtract(num1, num2)
            elif operation == "Multiply":
                result = multiply(num1, num2)
            elif operation == "Divide":
                result = divide(num1, num2)
            elif operation == "Sine":
                result = calculate_sine(num1)
            elif operation == "Cosine":
                result = calculate_cosine(num1)
            elif operation == "Logarithm":
                result = calculate_logarithm(num1)

            self.result_value.config(text=f"{result:.2f}")
            self.status_bar.config(text="Calculation successful", foreground="green")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            self.status_bar.config(text="Error: Invalid input", foreground="red")
        except ZeroDivisionError as e:
            messagebox.showerror("Math Error", str(e))
            self.status_bar.config(text="Error: Cannot divide by zero", foreground="red")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_bar.config(text="Error occurred", foreground="red")

    def clear_fields(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_value.config(text="")
        self.status_bar.config(text="Ready", foreground="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
