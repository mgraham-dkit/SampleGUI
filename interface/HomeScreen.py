import tkinter as tk
from tkinter.ttk import *

import LoginScreen
from model.user import User


class HomeScreen(tk.Frame):
    def __init__(self, root: tk.Tk, cur_user: User, users: dict[str, User]):
        tk.Frame.__init__(self, root)

        self.root = root
        self.cur_user = cur_user
        if users:
            self.users = users
        else:
            self.users: dict[str, User] = {}

        self.username_label = Label(self, text=f"Username: {cur_user.username}")
        self.back_button = Button(self, text="Back to login", command=self.show_login_screen)

        self.build()

    def build(self):
        # Fill with display field and button
        self.username_label.grid(row=0, column=0)
        self.back_button.grid(row=3, column=0, columnspan=2, pady=10)

    def show_login_screen(self):
        # Wipe the state information (user has logged out by going back to login screen)
        self.cur_user = None

        # Remove this frame from view
        self.pack_forget()
        # Show the login frame again
        login_screen = LoginScreen.LoginScreen(self.root, self.users)
        login_screen.pack(side="top", fill="both", expand=True)
        # Delete the current frame (avoids authentication context/state issues)
        self.destroy()
