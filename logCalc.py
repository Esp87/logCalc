# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:45:16 2025

@author: esp87
"""
import math
import tkinter as tk
from tkinter import messagebox

# Function to calculate logarithm
def calculate_log():
    try:
        base = float(base_entry.get())
        num = float(num_entry.get())
        
        if base <= 0 or base == 1 or num <= 0:
            messagebox.showerror("Error", "Base must be > 0 and ≠ 1, number must be > 0")
            return

        result = math.log(num) / math.log(base)
        exp_form = f"{base}^x = {num}"  # Exponential notation

        result_label.config(text=f"log_{base}({num}) = {result:.6f}")
        exp_label.config(text=f"Exponential Form: {exp_form}")

        # Store result in history
        history.insert(tk.END, f"log_{base}({num}) = {result:.6f}  |  {exp_form}\n")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Function to clear history
def clear_history():
    history.delete(1.0, tk.END)

# Create GUI window
root = tk.Tk()
root.title("Advanced Logarithm Calculator")
root.geometry("400x400")

# Labels and input fields
tk.Label(root, text="Base:").grid(row=0, column=0, padx=5, pady=5)
base_entry = tk.Entry(root)
base_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Number:").grid(row=1, column=0, padx=5, pady=5)
num_entry = tk.Entry(root)
num_entry.grid(row=1, column=1, padx=5, pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate_log)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result will be shown here", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=5)

# Exponential form label
exp_label = tk.Label(root, text="", font=("Arial", 10, "italic"))
exp_label.grid(row=4, column=0, columnspan=2, pady=5)

# History log
tk.Label(root, text="Calculation History:").grid(row=5, column=0, columnspan=2, pady=5)
history = tk.Text(root, height=8, width=45)
history.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Clear history button
clear_button = tk.Button(root, text="Clear History", command=clear_history)
clear_button.grid(row=7, column=0, columnspan=2, pady=5)

# Run the GUI loop
root.mainloop()

