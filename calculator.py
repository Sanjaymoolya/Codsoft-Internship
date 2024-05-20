import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 != 0:
            result = num1 / num2
            result_label.config(text=f"Result: {result}")
        else:
            messagebox.showerror("Error", "Division by zero is not allowed")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

# Main window setup
root = tk.Tk()
root.title("My Project Calculator")

# Input fields for numbers
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=10)

# Buttons for operations
tk.Button(root, text="Add", command=add).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=1, padx=10, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
