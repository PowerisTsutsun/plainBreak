import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox
from scripts.login_simulator import simulate_login
from scripts.dictionary_attack import dictionary_attack
from scripts.brute_force import brute_force_attack

# (rest of the code remains the same)


def run_login():
    username = username_entry.get()
    password = password_entry.get()
    if simulate_login(username, password):
        messagebox.showinfo("Login Result", f"Login successful for {username}")
    else:
        messagebox.showerror("Login Result", "Invalid credentials")

def run_dictionary_attack():
    cracked = dictionary_attack("data/users.db", "data/rockyou.txt")
    if cracked:
        result = "\n".join([f"{u}: {p}" for u, p in cracked])
        messagebox.showinfo("Dictionary Attack Result", result)
    else:
        messagebox.showinfo("Dictionary Attack Result", "No passwords cracked.")

def run_brute_force_attack():
    cracked = brute_force_attack("data/users.db", max_length=4)
    if cracked:
        result = "\n".join([f"{u}: {p}" for u, p in cracked])
        messagebox.showinfo("Brute-Force Attack Result", result)
    else:
        messagebox.showinfo("Brute-Force Attack Result", "No passwords cracked.")

# GUI Setup
root = tk.Tk()
root.title("PlainBreak: Cybersecurity Lab")

# Login Section
tk.Label(root, text="Simulated Login").grid(row=0, column=0, columnspan=2)
tk.Label(root, text="Username").grid(row=1, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1)
tk.Label(root, text="Password").grid(row=2, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1)
tk.Button(root, text="Login", command=run_login).grid(row=3, column=0, columnspan=2, pady=5)

# Attack Buttons
tk.Label(root, text="Attacks").grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Run Dictionary Attack", command=run_dictionary_attack).grid(row=5, column=0, columnspan=2, pady=2)
tk.Button(root, text="Run Brute-Force Attack", command=run_brute_force_attack).grid(row=6, column=0, columnspan=2, pady=2)

root.mainloop()
