import tkinter as tk
from tkinter import messagebox

# Store contacts in a list of dictionaries
contacts = []

# Add contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        messagebox.showinfo("Success", f"{name} added successfully!")
        clear_entries()
        display_contacts()
    else:
        messagebox.showwarning("Missing Info", "Name and Phone are required!")

# Clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Display all contacts
def display_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Search contact
def search_contact():
    keyword = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Delete selected contact
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contact_name = contacts[index]['name']
        del contacts[index]
        messagebox.showinfo("Deleted", f"{contact_name} deleted.")
        display_contacts()
    else:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")

# Update selected contact
def update_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contacts[index]['name'] = name_entry.get()
        contacts[index]['phone'] = phone_entry.get()
        contacts[index]['email'] = email_entry.get()
        contacts[index]['address'] = address_entry.get()
        messagebox.showinfo("Updated", "Contact updated successfully.")
        clear_entries()
        display_contacts()
    else:
        messagebox.showwarning("Select Contact", "Please select a contact to update.")

# Load contact on click
def load_contact(event):
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact['name'])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact['phone'])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact['email'])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact['address'])

# Main window
root = tk.Tk()
root.title("Contact Book - CodSoft Task")
root.geometry("600x500")
root.config(bg="#e3f2fd")

# Title label
tk.Label(root, text="📇 Contact Book", font=("Arial", 20, "bold"), bg="#e3f2fd", fg="#0d47a1").pack(pady=10)

# Form frame
form = tk.Frame(root, bg="#e3f2fd")
form.pack(pady=5)

tk.Label(form, text="Name:", bg="#e3f2fd").grid(row=0, column=0, sticky="e")
tk.Label(form, text="Phone:", bg="#e3f2fd").grid(row=1, column=0, sticky="e")
tk.Label(form, text="Email:", bg="#e3f2fd").grid(row=2, column=0, sticky="e")
tk.Label(form, text="Address:", bg="#e3f2fd").grid(row=3, column=0, sticky="e")

name_entry = tk.Entry(form, width=40)
phone_entry = tk.Entry(form, width=40)
email_entry = tk.Entry(form, width=40)
address_entry = tk.Entry(form, width=40)

name_entry.grid(row=0, column=1, pady=2)
phone_entry.grid(row=1, column=1, pady=2)
email_entry.grid(row=2, column=1, pady=2)
address_entry.grid(row=3, column=1, pady=2)

# Buttons
btn_frame = tk.Frame(root, bg="#e3f2fd")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add", width=10, bg="#64b5f6", command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=10, bg="#4db6ac", command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, bg="#ef5350", command=delete_contact).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Clear", width=10, bg="#ffca28", command=clear_entries).grid(row=0, column=3, padx=5)

# Search
search_frame = tk.Frame(root, bg="#e3f2fd")
search_frame.pack(pady=5)

search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side="left", padx=5)
tk.Button(search_frame, text="Search", bg="#90caf9", command=search_contact).pack(side="left")

# Contact list
contact_list = tk.Listbox(root, width=60, height=10)
contact_list.pack(pady=10)
contact_list.bind("<<ListboxSelect>>", load_contact)

# Show all contacts initially
display_contacts()

root.mainloop()
