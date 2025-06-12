import tkinter as tk

# Function to update expression
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

# Function to evaluate expression
def equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Clear screen
def clear():
    entry.delete(0, tk.END)

# Create window
root = tk.Tk()
root.title("Calculator - CodSoft")
root.geometry("320x450")
root.config(bg="#f0f8ff")

# Entry field
entry = tk.Entry(root, font=("Arial", 24), bd=4, relief=tk.RIDGE, justify='right', bg="white", fg="black")
entry.pack(pady=20, padx=10, fill="x")

# Button style
btn_style = {"font": ("Arial", 18), "bd": 2, "width": 5, "height": 2}

# Button frame
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack()

# Buttons layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

for row in buttons:
    btn_row = tk.Frame(frame, bg="#f0f8ff")
    btn_row.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: press(x) if x not in ['C', '='] else clear() if x == 'C' else equal()
        b = tk.Button(btn_row, text=btn, **btn_style, bg="#e6e6fa", fg="black", command=action)
        b.pack(side="left", expand=True, fill="both", padx=5, pady=5)

root.mainloop()
