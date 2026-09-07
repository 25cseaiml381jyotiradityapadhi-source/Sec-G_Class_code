import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

DB_NAME = "users.db"


def init_sqlite_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            role TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_user(name, email, role):
    if not name or not email or not role:
        messagebox.showwarning("Missing fields", "Name, email, and role are required.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (name, email, role) VALUES (?, ?, ?)",
            (name, email, role),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists.")
    else:
        messagebox.showinfo("Success", "User added successfully.")
    finally:
        conn.close()


def get_users():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, role FROM users ORDER BY id")
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_user(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()


class UserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Manager")
        self.root.geometry("620x420")
        self.root.resizable(False, False)

        self.build_form()
        self.build_table()
        self.load_users()

    def build_form(self):
        frame = ttk.LabelFrame(self.root, text="Add New User")
        frame.pack(fill="x", padx=16, pady=10)

        ttk.Label(frame, text="Name:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.name_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.name_var, width=28).grid(row=0, column=1, padx=8, pady=8)

        ttk.Label(frame, text="Email:").grid(row=0, column=2, padx=8, pady=8, sticky="w")
        self.email_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.email_var, width=28).grid(row=0, column=3, padx=8, pady=8)

        ttk.Label(frame, text="Role:").grid(row=1, column=0, padx=8, pady=8, sticky="w")
        self.role_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.role_var, width=28).grid(row=1, column=1, padx=8, pady=8)

        add_button = ttk.Button(frame, text="Add User", command=self.on_add_user)
        add_button.grid(row=1, column=3, padx=8, pady=8, sticky="e")

    def build_table(self):
        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        columns = ("id", "name", "email", "role")
        self.user_table = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        self.user_table.heading("id", text="ID")
        self.user_table.heading("name", text="Name")
        self.user_table.heading("email", text="Email")
        self.user_table.heading("role", text="Role")
        self.user_table.column("id", width=50, anchor="center")
        self.user_table.column("name", width=150)
        self.user_table.column("email", width=220)
        self.user_table.column("role", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.user_table.yview)
        self.user_table.configure(yscroll=scrollbar.set)
        self.user_table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill="x", padx=16, pady=(0, 16))

        refresh_button = ttk.Button(button_frame, text="Refresh", command=self.load_users)
        refresh_button.pack(side="left")

        delete_button = ttk.Button(button_frame, text="Delete Selected", command=self.on_delete_user)
        delete_button.pack(side="right")

    def on_add_user(self):
        add_user(self.name_var.get().strip(), self.email_var.get().strip(), self.role_var.get().strip())
        self.name_var.set("")
        self.email_var.set("")
        self.role_var.set("")
        self.load_users()

    def load_users(self):
        for row in self.user_table.get_children():
            self.user_table.delete(row)

        for user in get_users():
            self.user_table.insert("", "end", values=user)

    def on_delete_user(self):
        selected = self.user_table.selection()
        if not selected:
            messagebox.showwarning("No selection", "Select a user to delete.")
            return

        user_id = self.user_table.item(selected[0], "values")[0]
        if messagebox.askyesno("Confirm", "Delete selected user?"):
            delete_user(user_id)
            self.load_users()


if __name__ == "__main__":
    init_sqlite_db()
    root = tk.Tk()
    app = UserApp(root)
    root.mainloop()

