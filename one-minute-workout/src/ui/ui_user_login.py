from tkinter import ttk, messagebox
from user import User
from ui.ui_timer import UITimer


class UIUserLogin:
    """Class for user login UI.

    Attributes:
        root: Tk() main window defined in the application class
    """

    def __init__(self, root):
        """Class constructor to create user login UI.

        Args:
            root: Tk() main window defined in the application class
            username: username string saved in the users.json
            password: password string saved with username in the users.json
            login_frame: frame for login related widgets
            quit_frame: frame for application exit related widgets
        """
        self.root = root
        self.username = None
        self.password = None
        self.login_frame = None
        self.quit_frame = None

    def start(self):
        """Start and define the user login UI.

        Username and password entries and login, cancel and quit the app buttons.
        """
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
                                  command=self._user_login_json)
        cancel_button = ttk.Button(master=self.login_frame, text="Cancel",
                                   command=self._cancel)

        login_button.pack(pady=10)
        cancel_button.pack(pady=10)

        self.quit_frame = ttk.Frame(master=self.root)
        self.quit_frame.pack()

        quit_button = ttk.Button(master=self.quit_frame, text="Quit the app",
                                 command=self.root.destroy)

        quit_button.pack(pady=50)

    def _user_login_json(self):
        """Check if the user exists in users.json file and if the password entry matches the username"""
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

    def _cancel(self):
        """Clear the login UI entries"""
        self.username.delete(0, "end")
        self.password.delete(0, "end")
