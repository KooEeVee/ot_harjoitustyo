from tkinter import ttk, messagebox
from user import User
from ui.ui_timer import UITimer


class UIUserLogin:
    def __init__(self, root):
        self.root = root
        self.username = None
        self.password = None

    def start(self):
        username_label = ttk.Label(master=self.root, text="Your username")
        self.username = ttk.Entry(master=self.root)
        password_label = ttk.Label(master=self.root, text="Your password")
        self.password = ttk.Entry(master=self.root)
        login_button = ttk.Button(master=self.root, text="Log in",
                            command=self.button_click_to_login_json)
        cancel_button = ttk.Button(master=self.root, text="Cancel",
                            command=self.button_click_to_cancel)

        username_label.pack()
        self.username.pack()
        password_label.pack()
        self.password.pack()
        login_button.pack()
        cancel_button.pack()

    def button_click_to_login_json(self):
        username_value = self.username.get()
        password_value = self.password.get()
        user = User(username_value, password_value)
        if user.get_user_json():
            if password_value == user.get_password_json(username_value):
                goodbye = ttk.Label(master=self.root, text="Login successful, welcome!")
                goodbye.pack()
            else:
                messagebox.showinfo("Wrong password", "Please try again")
                self.password.delete(0, "end")
        else:
            messagebox.showinfo("User not found", "Please try again")
            self.username.delete(0, "end")
            self.password.delete(0, "end")

        timer = UITimer(self.root, self.username)  
        timer.start()

    def button_click_to_cancel(self):
        self.username.delete(0, "end")
        self.password.delete(0, "end")

    # def button_click_to_login_csv(self):
    #     username_value = self.username.get()
    #     password_value = self.password.get()
    #     user = User(username_value, password_value)
    #     if user.get_username_csv(username_value) == True:
    #         if password_value == user.get_password_csv(username_value):
    #             goodbye = ttk.Label(master=self.root, text="Login successful, welcome!")
    #             goodbye.pack()
    #         else:
    #             messagebox.showinfo("Wrong password", "Please try again")
    #             self.password.delete(0, "end")
    #     else:
    #         messagebox.showinfo("User not found", "Please try again")
    #         self.username.delete(0, "end")
    #         self.password.delete(0, "end")
    
    
    # def button_click_to_login_db(self):
    #     username_value = self.username.get()
    #     password_value = self.password.get()
    #     user = User(username_value, password_value)
        
    #     if username_value == user.get_username_db(username_value):
    #         if password_value == user.get_password_db(username_value):
    #             goodbye = ttk.Label(master=self.root, text="Login successful, welcome!")
    #             goodbye.pack()
    #         else:
    #             messagebox.showinfo("Wrong password", "Please try again")
    #             self.username.delete(0, "end")
    #             self.password.delete(0, "end")
    #     else:
    #         messagebox.showinfo("User not found", "Please try again")
    #         self.username.delete(0, "end")
    #         self.password.delete(0, "end")

        
        