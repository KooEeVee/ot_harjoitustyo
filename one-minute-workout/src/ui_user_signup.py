from tkinter import Tk, ttk
from user import User

class UIUserSignup:
    def __init__(self, root):
        self.root = root
        self.username = None
        self.password = None

    def start(self):
        username_label = ttk.Label(master=self.root, text="Your username")
        self.username = ttk.Entry(master=self.root)
        password_label = ttk.Label(master=self.root, text="Your password")
        self.password = ttk.Entry(master=self.root)
        button = ttk.Button(master=self.root, text="Sign up", command=self.button_click_to_csv)

        username_label.pack()
        self.username.pack()
        password_label.pack()
        self.password.pack()
        button.pack()

    def button_click_to_csv(self):
        username_value = self.username.get()
        password_value = self.password.get()
        user = User(username_value, password_value)
        user.newUser()
        goodbye = ttk.Label(master=self.root, text="Thank you for signing up!")
        goodbye.pack()
        self.username.delete(0, "end")
        self.password.delete(0, "end")
        