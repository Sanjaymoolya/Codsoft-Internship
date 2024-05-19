import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Password length must be at least 1")
        
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()

        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated password: {password}")

    except ValueError as ve:
        messagebox.showerror("Invalid input", str(ve))

# Main window setup
root = tk.Tk()
root.title(" CodSoft Password Generator")

# Length input
tk.Label(root, text="Enter the desired length of the password:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Options for complexity
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='w')
tk.Checkbutton(root, text="Include digits", variable=digits_var).grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='w')
tk.Checkbutton(root, text="Include special characters", variable=special_var).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='w')

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Generated password: ")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
