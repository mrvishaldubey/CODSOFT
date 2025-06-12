import tkinter as tk
from tkinter import messagebox

# -------- Functions -------- #
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "No task selected!")

def mark_done():
    try:
        selected = listbox.curselection()
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(tk.END, f"✔️ {task}")
    except:
        messagebox.showwarning("Warning", "No task selected!")

# -------- GUI -------- #
root = tk.Tk()
root.title("To-Do List App - CodSoft")
root.geometry("400x500")
root.config(bg="#83baeb")

# Title
title = tk.Label(root, text="📝 To-Do List", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#333")
title.pack(pady=10)

# Entry
entry = tk.Entry(root, font=("Helvetica", 14), width=24, bd=2)
entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=5)

add_btn = tk.Button(button_frame, text="Add Task", width=10, bg="#4CAF50", fg="white", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

done_btn = tk.Button(button_frame, text="Mark Done", width=10, bg="#2196F3", fg="white", command=mark_done)
done_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Task", width=10, bg="#f44336", fg="white", command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, font=("Helvetica", 14), width=32, height=15, bd=2, fg="#333")
listbox.pack(pady=20)

# Start App
root.mainloop()
