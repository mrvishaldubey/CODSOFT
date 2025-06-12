import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid password length.")

# Function to copy password
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator - CodSoft Task")
root.geometry("400x300")
root.config(bg="#f1f8e9")

tk.Label(root, text="🔐 Password Generator", font=("Arial", 20, "bold"), fg="#33691e", bg="#f1f8e9").pack(pady=10)

# Password length
tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#f1f8e9").pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 14), justify='center')
length_entry.pack(pady=5)

# Generate button
tk.Button(root, text="Generate", font=("Arial", 12), bg="#aed581", command=generate_password).pack(pady=10)

# Show password
password_entry = tk.Entry(root, font=("Arial", 14), justify='center', width=30)
password_entry.pack(pady=10)

# Copy button
tk.Button(root, text="Copy Password", font=("Arial", 12), bg="#81d4fa", command=copy_password).pack(pady=5)

root.mainloop()
