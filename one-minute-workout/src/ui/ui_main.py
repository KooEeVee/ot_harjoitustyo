from tkinter import Tk, ttk, messagebox
from ui.ui_user_signup import UIUserSignup
from ui.ui_user_login import UIUserLogin

class UIMain:
    """Class for application launch UI.
    
    Attributes:
        root: Tk() main window defined in the application class
    """
    def __init__(self, root):
        """Class constructor to create an application launch UI.

        Args:
            root: Tk() main window defined in the application class
            signup_frame: frame for signup related widgets
            login_frame: frame for login related widgets
            quit_frame: frame for application exit related widgets
        """
        self.root = root
        self.signup_frame = None
        self.login_frame = None
        self.quit_frame = None

    def start(self):
        """Start and define the application launch UI.
        
        Signup, login and quit the app buttons.
        """
        self.signup_frame = ttk.Frame(master=self.root)
        self.signup_frame.pack()

        signup_label = ttk.Label(
            master=self.signup_frame, text="I'm a new user", font=("Helvetica", 12))
        signup_button = ttk.Button(master=self.signup_frame, text="Sign up",
                                   command=self._signup)

        signup_label.pack(pady=10)
        signup_button.pack()

        self.login_frame = ttk.Frame(master=self.root)
        self.login_frame.pack()

        login_label = ttk.Label(master=self.login_frame,
                                text="I already have an account", font=("Helvetica", 12))
        login_button = ttk.Button(master=self.login_frame, text="Log in",
                                  command=self._login)

        login_label.pack(pady=10)
        login_button.pack()

        self.quit_frame = ttk.Frame(master=self.root)
        self.quit_frame.pack()

        quit_button = ttk.Button(master=self.quit_frame, text="Quit the app",
                                 command=self.root.destroy)

        quit_button.pack(pady=50)

    def _signup(self):
        """Start the user signup UI and close the application launch UI"""
        signup = UIUserSignup(self.root)
        self.signup_frame.destroy()
        self.login_frame.destroy()
        self.quit_frame.destroy()
        signup.start()

    def _login(self):
        """Start the user login UI and close the application launch UI"""
        login = UIUserLogin(self.root)
        self.signup_frame.destroy()
        self.login_frame.destroy()
        self.quit_frame.destroy()
        login.start()
