import tkinter as tk
from tkinter import messagebox, simpledialog

# Contact book class to manage contacts
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})

    def get_contacts(self):
        return self.contacts

    def search_contact(self, query):
        return [contact for contact in self.contacts if query.lower() in contact["name"].lower() or query in contact["phone"]]

    def update_contact(self, index, name, phone, email, address):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            return True
        return False

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            return True
        return False

# Functions to handle GUI interactions
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact_book.add_contact(name, phone, email, address)
        messagebox.showinfo("Success", "Contact added successfully")
        update_contact_list()
    else:
        messagebox.showerror("Error", "Name and Phone are required")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contact_book.get_contacts():
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    query = search_entry.get()
    results = contact_book.search_contact(query)
    contact_list.delete(0, tk.END)
    for contact in results:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def on_contact_select(event):
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        contact = contact_book.get_contacts()[index]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact['name'])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact['phone'])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact['email'])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact['address'])

def update_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        if contact_book.update_contact(index, name, phone, email, address):
            messagebox.showinfo("Success", "Contact updated successfully")
            update_contact_list()
        else:
            messagebox.showerror("Error", "Failed to update contact")

def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        if contact_book.delete_contact(index):
            messagebox.showinfo("Success", "Contact deleted successfully")
            update_contact_list()
        else:
            messagebox.showerror("Error", "Failed to delete contact")

# Main window setup
root = tk.Tk()
root.title("Contact Book")

contact_book = ContactBook()

# Contact form
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2, pady=10)

# Contact list
tk.Label(root, text="Contact List:").grid(row=0, column=2, padx=10, pady=5)
contact_list = tk.Listbox(root)
contact_list.grid(row=1, column=2, rowspan=4, padx=10, pady=5)
contact_list.bind('<<ListboxSelect>>', on_contact_select)

# Search bar
tk.Label(root, text="Search:").grid(row=5, column=0, padx=10, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=5, column=1, padx=10, pady=5)
tk.Button(root, text="Search", command=search_contact).grid(row=5, column=2, padx=10, pady=5)

# Update and delete buttons
tk.Button(root, text="Update Contact", command=update_contact).grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=6, column=2, pady=5)

# Start the main loop
root.mainloop()
