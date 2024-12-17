import tkinter as tk
from tkinter import messagebox
import random
import string

# Define color mappings to character sets
color_map = {
    "red": string.ascii_uppercase,     # Red = uppercase letters
    "blue": string.ascii_lowercase,    # Blue = lowercase letters
    "green": string.digits,            # Green = numbers
    "yellow": string.punctuation       # Yellow = special characters
}

# Function to generate password
def generate_password():
    selected_colors = []
    if red_var.get():
        selected_colors.append("red")
    if blue_var.get():
        selected_colors.append("blue")
    if green_var.get():
        selected_colors.append("green")
    if yellow_var.get():
        selected_colors.append("yellow")
    
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a number.")
        return
    
    if not selected_colors:
        messagebox.showerror("No Colors Selected", "Please select at least one color.")
        return
    
    if length < len(selected_colors):
        messagebox.showerror("Invalid Length", "Length must be greater than or equal to the number of selected colors.")
        return

    # Generate the password
    password = []
    for color in selected_colors:
        password.append(random.choice(color_map[color]))
    all_chars = ''.join(color_map[color] for color in selected_colors)
    for _ in range(length - len(password)):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    
    # Display the generated password
    password_display.config(text="Generated Password: " + ''.join(password))

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# Add title label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Add instructions
instructions_label = tk.Label(root, text="Select colors and specify password length.", font=("Arial", 12))
instructions_label.pack(pady=5)

# Add checkboxes for colors
red_var = tk.BooleanVar()
blue_var = tk.BooleanVar()
green_var = tk.BooleanVar()
yellow_var = tk.BooleanVar()

checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=10)

tk.Checkbutton(checkbox_frame, text="Red (Uppercase Letters)", variable=red_var).grid(row=0, column=0, sticky="w")
tk.Checkbutton(checkbox_frame, text="Blue (Lowercase Letters)", variable=blue_var).grid(row=1, column=0, sticky="w")
tk.Checkbutton(checkbox_frame, text="Green (Numbers)", variable=green_var).grid(row=2, column=0, sticky="w")
tk.Checkbutton(checkbox_frame, text="Yellow (Special Characters)", variable=yellow_var).grid(row=3, column=0, sticky="w")

# Add entry for password length
length_frame = tk.Frame(root)
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 12))
length_label.pack(side="left")

length_entry = tk.Entry(length_frame, width=5)
length_entry.pack(side="left", padx=5)

# Add button to generate password
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), command=generate_password)
generate_button.pack(pady=20)

# Add label to display the password
password_display = tk.Label(root, text="", font=("Arial", 12), wraplength=380, fg="blue")
password_display.pack(pady=10)

# Run the application
root.mainloop()
