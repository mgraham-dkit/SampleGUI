import tkinter as tk
from LoginScreen import LoginScreen
from model.user import User


def load_model(filename: str) -> dict[User]:
    users = {}
    try:
        with open(filename) as file:
            for line in file:
                username, password = line.strip().split("%%")
                try:
                    user = User(username, password)
                    if username in users:
                        print(f"Username \'{username}\' already exists.")
                    else:
                        users[username] = user
                except ValueError as e:
                    print(f"Problem restoring user '{username}': password is too weak.")

    except FileNotFoundError as e:
        raise FileNotFoundError("User data file does not exist")

    return users


loaded = False
users = {}
while not loaded:
    filename = input("Please enter the user data filename: ")
    try:
        users = load_model(filename)
    except FileNotFoundError as e:
        print("Issue when reading in from user data file: " + e.__str__())
    else:
        loaded = True

print("Userbase loaded.")
root_window = tk.Tk()
loginScreen = LoginScreen(root_window, users)
# Trigger the GUI to start listening for user interaction
root_window.mainloop()