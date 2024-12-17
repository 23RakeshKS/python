import tkinter as tk
from tkinter import messagebox
import csv

# Global variable to manage frames
current_frame = None

# Function to handle signup
def sign_up():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        # Check if the username already exists
        with open("users.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    messagebox.showerror("Error", "Username already exists!")
                    return

        # Save the new user to CSV
        with open("users.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        messagebox.showinfo("Success", "Sign up successful! Please log in.")
        login_screen()  # Switch to login screen
    else:
        messagebox.showerror("Error", "Please enter both username and password")

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password")
        return

    with open("users.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                main_menu(username)
                return

    messagebox.showerror("Error", "Invalid username or password")

# Function for the main menu and food order
def main_menu(username):
    global current_frame
    if current_frame:
        current_frame.pack_forget()

    main_menu_frame = tk.Frame(root, bg='lightblue')
    main_menu_frame.pack(fill=tk.BOTH, expand=True)

    label_welcome = tk.Label(main_menu_frame, text=f"Welcome, {username}!", font=("Arial", 20), bg='lightblue')
    label_welcome.pack(pady=20)

    label_menu = tk.Label(main_menu_frame, text="South Indian Food Menu", font=("Arial", 18), bg='lightblue')
    label_menu.pack(pady=10)

    menu = {
        "Idli": 50,
        "Dosa": 80,
        "Sambar Vada": 60,
        "Pongal": 70,
        "Uttapam": 90
    }

    item_buttons = []
    for item, price in menu.items():
        button = tk.Button(main_menu_frame, text=f"{item} - ₹{price}", font=("Arial", 14), bg='yellow', command=lambda item=item, price=price: add_to_order(item, price))
        button.pack(pady=5)
        item_buttons.append(button)

    label_total = tk.Label(main_menu_frame, text="Total: ₹0", font=("Arial", 16), bg='lightblue')
    label_total.pack(pady=20)

    total_price = 0

    def add_to_order(item, price):
        nonlocal total_price
        total_price += price
        label_total.config(text=f"Total: ₹{total_price}")

    # Checkout Button
    def checkout():
        messagebox.showinfo("Order Summary", f"Total Amount: ₹{total_price}")
        main_menu_frame.pack_forget()
        login_screen()

    checkout_button = tk.Button(main_menu_frame, text="Checkout", font=("Arial", 14), bg='green', command=checkout)
    checkout_button.pack(pady=20)

    current_frame = main_menu_frame

# Login Screen
def login_screen():
    global entry_username, entry_password, current_frame

    if current_frame:
        current_frame.pack_forget()

    login_frame = tk.Frame(root, bg='lightgreen')
    login_frame.pack(fill=tk.BOTH, expand=True)

    label_title = tk.Label(login_frame, text="Hotel Management System", font=("Arial", 24), bg='lightgreen')
    label_title.pack(pady=30)

    label_username = tk.Label(login_frame, text="Username", font=("Arial", 14), bg='lightgreen')
    label_username.pack(pady=5)
    entry_username = tk.Entry(login_frame, font=("Arial", 14))
    entry_username.pack(pady=5)

    label_password = tk.Label(login_frame, text="Password", font=("Arial", 14), bg='lightgreen')
    label_password.pack(pady=5)
    entry_password = tk.Entry(login_frame, font=("Arial", 14), show="*")
    entry_password.pack(pady=5)

    login_button = tk.Button(login_frame, text="Login", font=("Arial", 14), bg='blue', command=login)
    login_button.pack(pady=20)

    sign_up_button = tk.Button(login_frame, text="Sign Up", font=("Arial", 14), bg='orange', command=sign_up_screen)
    sign_up_button.pack(pady=10)

    current_frame = login_frame

# Sign-up Screen
def sign_up_screen():
    global entry_username, entry_password, current_frame

    if current_frame:
        current_frame.pack_forget()

    sign_up_frame = tk.Frame(root, bg='lightyellow')
    sign_up_frame.pack(fill=tk.BOTH, expand=True)

    label_title = tk.Label(sign_up_frame, text="Create New Account", font=("Arial", 24), bg='lightyellow')
    label_title.pack(pady=30)

    label_username = tk.Label(sign_up_frame, text="Username", font=("Arial", 14), bg='lightyellow')
    label_username.pack(pady=5)
    entry_username = tk.Entry(sign_up_frame, font=("Arial", 14))
    entry_username.pack(pady=5)

    label_password = tk.Label(sign_up_frame, text="Password", font=("Arial", 14), bg='lightyellow')
    label_password.pack(pady=5)
    entry_password = tk.Entry(sign_up_frame, font=("Arial", 14), show="*")
    entry_password.pack(pady=5)

    sign_up_button = tk.Button(sign_up_frame, text="Sign Up", font=("Arial", 14), bg='blue', command=sign_up)
    sign_up_button.pack(pady=20)

    login_button = tk.Button(sign_up_frame, text="Already have an account? Login", font=("Arial", 14), bg='green', command=login_screen)
    login_button.pack(pady=10)

    current_frame = sign_up_frame

# Root Window
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("600x600")
root.config(bg="lightgreen")

login_screen()  # Start with the login screen
root.mainloop()
