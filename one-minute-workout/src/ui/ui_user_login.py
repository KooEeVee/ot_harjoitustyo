from tkinter import ttk, messagebox
from user import User
from ui.ui_timer import UITimer

class UIUserLogin:
    def __init__(self, root):
        self.root = root
        self.username = None
        self.password = None
        self.login_frame = None
        self.quit_frame = None

    def start(self):
        self.login_frame = ttk.Frame(master=self.root)
        self.login_frame.pack()

        username_label = ttk.Label(
            master=self.login_frame, text="Your username", font=("Helvetica", 12))
        self.username = ttk.Entry(master=self.login_frame)

        username_label.pack(pady=10)
        self.username.pack()

        password_label = ttk.Label(
            master=self.login_frame, text="Your password", font=("Helvetica", 12))
        self.password = ttk.Entry(master=self.login_frame, show="*")

        password_label.pack(pady=10)
        self.password.pack()

        login_button = ttk.Button(master=self.login_frame, text="Log in",
                                  command=self.user_login_json)
        cancel_button = ttk.Button(master=self.login_frame, text="Cancel",
                                   command=self.cancel)

        login_button.pack(pady=10)
        cancel_button.pack(pady=10)

        self.quit_frame = ttk.Frame(master=self.root)
        self.quit_frame.pack()

        # quit_label = ttk.Label(master=self.quit_frame,
        #                        text="Exit the app", font=("Helvetica", 12))
        quit_button = ttk.Button(master=self.quit_frame, text="Quit the app",
                                 command=self.root.destroy)

        # quit_label.pack(pady=10)
        quit_button.pack(pady=50)

    def user_login_json(self):
        username_value = self.username.get()
        password_value = self.password.get()
        user = User(username_value, password_value)
        if user.get_user_json():
            if password_value == user.get_password_json(username_value):
                timer = UITimer(self.root, username_value)
                timer.start()
                self.login_frame.destroy()
                self.quit_frame.destroy()

            else:
                messagebox.showinfo("Wrong password", "Please try again")
                self.password.delete(0, "end")
        else:
            messagebox.showinfo("User not found", "Please try again")
            self.username.delete(0, "end")
            self.password.delete(0, "end")

    def cancel(self):
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
