import math
import tkinter as tk
from tkinter import Label, Entry, Button, Frame


def main():
    # Create the root window
    root = tk.Tk()
    root.title("Circle Area Calculator")

    # Create the main frame
    frm_main = Frame(root)
    frm_main.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Populate the main window with widgets
    populate_main_window(frm_main)

    # Start the Tkinter event loop
    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window with labels, text entry boxes, and buttons."""

    # Create labels and input fields for radius and area
    lbl_radius = Label(frm_main, text="Radius:")
    lbl_area = Label(frm_main, text="Area:")

    ent_radius = Entry(frm_main, width=10)
    lbl_result = Label(frm_main, text="", width=20, anchor="w")

    # Create buttons for calculate and clear
    btn_calculate = Button(frm_main, text="Calculate")
    btn_clear = Button(frm_main, text="Clear")

    # Arrange widgets in a grid layout
    lbl_radius.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    ent_radius.grid(row=0, column=1, padx=5, pady=5)
    lbl_area.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    lbl_result.grid(row=1, column=1, padx=5, pady=5)
    btn_calculate.grid(row=2, column=0, padx=5, pady=5)
    btn_clear.grid(row=2, column=1, padx=5, pady=5)

    # Function to calculate the area of a circle
    def calculate():
        """Calculate and display the area of the circle."""
        try:
            radius = float(ent_radius.get())
            if radius < 0:
                lbl_result.config(text="Error: Radius must be positive.")
            else:
                area = math.pi * radius ** 2
                lbl_result.config(text=f"{area:.2f}")
        except ValueError:
            lbl_result.config(text="Error: Invalid input.")

    # Function to clear all inputs and outputs
    def clear():
        """Clear the input and output fields."""
        ent_radius.delete(0, tk.END)
        lbl_result.config(text="")

    # Bind functions to buttons
    btn_calculate.config(command=calculate)
    btn_clear.config(command=clear)


# Call main to start the program
if __name__ == "__main__":
    main()
