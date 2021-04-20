from tkinter import ttk, messagebox
from ui_user_signup import UIUserSignup
from ui_user_login import UIUserLogin

class UIMain:
    def __init__(self, root):
        self.root = root


    def start(self):

        upperframe = ttk.Frame(master=self.root)
        upperframe.pack()

        lowerframe = ttk.Frame(master=self.root)
        lowerframe.pack()

    #     signup_label = ttk.Label(master=self.root, text="I'm a new user")
    #     button = ttk.Button(master=self.root, text="Sign up",
    #                         command=self.button_click_to_csv)
    #     password_label = ttk.Label(master=self.root, text="Your password")
    #     self.password = ttk.Entry(master=self.root)
    #     button = ttk.Button(master=self.root, text="Sign up",
    #                         command=self.button_click_to_csv)

    #     username_label.pack()
    #     self.username.pack()
    #     password_label.pack()
    #     self.password.pack()
    #     button.pack()
    
    # def button_click_signup(self):
    #     signup = UIUserSignup()
    #     goodbye = ttk.Label(master=self.root, text="Thank you for signing up!")
    #     goodbye.pack()
    #     self.username.delete(0, "end")
    #     self.password.delete(0, "end")