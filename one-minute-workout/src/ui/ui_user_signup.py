from tkinter import ttk, messagebox
from user import User
from ui.ui_timer import UITimer

class UIUserSignup:
    """Class for user signup UI.
    
    Attributes:
        root: Tk() main window defined in the application class
    """
    def __init__(self, root):
        """Class constructor to create user signup UI.

        Args:
            root: Tk() main window defined in the application class
            username: username string entry to be saved in the users.json
            password: password string entry to be saved with username in the users.json
            signup_frame: frame for signup related widgets
            quit_frame: frame for application exit related widgets
        """
        self.root = root
        self.username = None
        self.password = None
        self.signup_frame = None
        self.quit_frame = None

    def start(self):
        """Start and define the user signup UI.
        
        Username and password entries and signup, cancel and quit the app buttons.
        """
        self.signup_frame = ttk.Frame(master=self.root)
        self.signup_frame.pack()

        username_label = ttk.Label(
            master=self.signup_frame, text="Your username", font=("Helvetica", 12))
        self.username = ttk.Entry(master=self.signup_frame)

        username_label.pack(pady=10)
        self.username.pack()

        password_label = ttk.Label(
            master=self.signup_frame, text="Your password", font=("Helvetica", 12))
        self.password = ttk.Entry(master=self.signup_frame)

        password_label.pack(pady=10)
        self.password.pack()

        signup_button = ttk.Button(master=self.signup_frame, text="Sign up",
                                   command=self._save_user_to_json)
        cancel_button = ttk.Button(master=self.signup_frame, text="Cancel",
                                   command=self._cancel)

        signup_button.pack(pady=10)
        cancel_button.pack(pady=10)

        self.quit_frame = ttk.Frame(master=self.root)
        self.quit_frame.pack()

        quit_button = ttk.Button(master=self.quit_frame, text="Quit the app",
                                 command=self.root.destroy)

        quit_button.pack(pady=50)

    def _save_user_to_json(self):
        """Save user signup entries to users.json file.
        
        Checks for username already in use, username length and password length.
        """
        username_value = self.username.get()
        password_value = self.password.get()
        user = User(username_value, password_value)
        if user.get_user_json():
            messagebox.showinfo("Username is already taken",
                                "Please choose another")
            self.username.delete(0, "end")
            self.password.delete(0, "end")
        else:
            if len(username_value) > 0:
                if len(password_value) > 0:
                    user.new_user_json()
                    timer = UITimer(self.root, username_value)
                    timer.start()
                    self.signup_frame.destroy()
                    self.quit_frame.destroy()

                else:
                    messagebox.showinfo("Password empty", "Please try again")
                    self.password.delete(0, "end")
            else:
                messagebox.showinfo("Username empty", "Please try again")
                self.username.delete(0, "end")
                self.password.delete(0, "end")

    def _cancel(self):
        """Clear the signup UI entries"""
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
