from tkinter import ttk, messagebox
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
        button = ttk.Button(master=self.root, text="Sign up",
                            command=self.button_click_save_to_json)

        username_label.pack()
        self.username.pack()
        password_label.pack()
        self.password.pack()
        button.pack()

    def button_click_save_to_json(self):
        username_value = self.username.get()
        password_value = self.password.get()
        user = User(username_value, password_value)
        if user.get_user_json(username_value):
            messagebox.showinfo("Username is already taken", "Please choose another")
            self.username.delete(0, "end")
            self.password.delete(0, "end")
        else:
            if len(username_value) > 0:
                if len(password_value) > 0:
                    user.new_user_json()
                    thankyou = ttk.Label(
                        master=self.root, text="Thank you for signing up!")
                    thankyou.pack()
                    self.username.delete(0, "end")
                    self.password.delete(0, "end")
                else:
                    messagebox.showinfo("Password empty", "Please try again")
                    self.password.delete(0, "end")
            else:
                messagebox.showinfo("Username empty", "Please try again")
                self.username.delete(0, "end")
                self.password.delete(0, "end")

    # def button_click_save_to_csv(self):
    #     username_value = self.username.get()
    #     password_value = self.password.get()
    #     user = User(username_value, password_value)
    #     if user.get_username_csv(username_value):
    #         messagebox.showinfo("Username is already taken", "Please choose another")
    #         self.username.delete(0, "end")
    #         self.password.delete(0, "end")
    #     else:
    #         if len(username_value) > 0:
    #             if len(password_value) > 0:
    #                 user.new_user_csv()
    #                 thankyou = ttk.Label(
    #                     master=self.root, text="Thank you for signing up!")
    #                 thankyou.pack()
    #                 self.username.delete(0, "end")
    #                 self.password.delete(0, "end")
    #             else:
    #                 messagebox.showinfo("Password empty", "Please try again")
    #                 self.password.delete(0, "end")
    #         else:
    #             messagebox.showinfo("Username empty", "Please try again")
    #             self.username.delete(0, "end")
    #             self.password.delete(0, "end")

    # def button_click_to_db(self):
    #     username_value = self.username.get()
    #     password_value = self.password.get()
    #     user = User(username_value, password_value)
    #     user.new_user_db()
    #     goodbye = ttk.Label(master=self.root, text="Thank you for signing up!")
    #     goodbye.pack()
    #     self.username.delete(0, "end")
    #     self.password.delete(0, "end")
