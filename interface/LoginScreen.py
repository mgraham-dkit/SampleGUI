import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from model.user import User
import HomeScreen


class LoginScreen(tk.Frame):
    # Create default admin information
    admin_user = "admin"
    admin_pass = "adminPass1"

    def __init__(self, root: tk.Tk, users: dict[str, User] = None):
        tk.Frame.__init__(self, root)
        self.root = root
        # If no user dictionary was provided, make a blank one
        if users is None:
            self.users: dict[str, User] = {}
        else:
            self.users = users

        # Create a variable to track if the text is currently being hidden by *
        self.hidden = True

        # Create the window components (do not place them yet)

        # Username details
        self.username_label = Label(self, text="Username: ")
        self.username_field = Entry(self)
        # Password details
        self.password_label = Label(self, text="Password: ")
        self.password_field = Entry(self, show="*")

        # Create buttons for login, register and show/hide password (toggles visibility)
        self.show_button = Button(self, text="Show password", command=self.toggle)
        self.login_button = Button(self, text="Login", command=self.login_command)
        self.register_button = Button(self, text="Register", command=self.register_command)

        # Build the screen components within that window
        self.build()

    def build(self):
        # Load this frame into the window
        self.pack(side="top", fill="both", expand=True)
        # Make the username and password components visible
        self.username_label.grid(row=0, column=0)
        self.username_field.grid(row=0, column=1, padx=10)
        self.password_label.grid(row=1, column=0)
        self.password_field.grid(row=1, column=1, padx=10)

        # Toggle visibility details
        self.show_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Make the login and register buttons visible
        self.login_button.grid(row=4, column=0, columnspan=1, pady=10)
        self.register_button.grid(row=4, column=1, columnspan=1, pady=10)

    def toggle(self):
        # If the text is currently hidden
        if self.hidden:
            # Change the setting on the text field to show the content as cleartext
            self.password_field.config(show="")
            # Change the text displayed on the button to say it will HIDE the password next time
            self.show_button.config(text="Hide password")
            # Mark the text as currently not being hidden
            self.hidden = False
        # Otherwise
        else:
            # Set the text field to show *s and hide the actual text of the password
            self.password_field.config(show="*")
            # Change the button to say it will SHOW the password next time
            self.show_button.config(text="Show password")
            # Mark the text as currently being hidden
            self.hidden = True

    def login_command(self):
        username = self.username_field.get()
        self.username_field.delete(0, tk.END)
        password = self.password_field.get()
        self.password_field.delete(0, tk.END)

        if username and password:
            result = self.login(username, password)
            if result[0]:
                messagebox.showinfo("Success", "Login successful!")
                # Remember to pass the user data and current user to that screen
                home_screen = HomeScreen(self.root, result[1], self.users)
                # Remember to hide THIS screen.
                self.pack_forget()
                home_screen.pack(side="top", fill="both", expand=True)
                self.destroy()
            else:
                messagebox.showerror("Failure", "Incorrect username or password supplied!")
        else:
            messagebox.showwarning("Warning", "Please complete all fields.")

    def login(self, username: str, password:str) -> tuple[bool, User|None]:
        if username.lower() == LoginScreen.admin_user.lower() and password == LoginScreen.admin_pass:
            is_admin = True
            cur_user = User(username, password)
            return True, cur_user
        elif username in self.users:
            user = self.users[username]
            if user.authenticate(password):
                return True, user
            else:
                return False, None
        else:
            return False, None

    def register_command(self):
        pass
        # todo: Write logic to register a new user


if __name__ == "__main__":
    sample_user = "username"
    sample_pass = "password"
    user_dict = {sample_user : User(sample_user, sample_pass)}

    root_window = tk.Tk()
    screen = LoginScreen(root_window, user_dict)

    # Trigger the GUI to start listening for user interaction
    root_window.mainloop()
