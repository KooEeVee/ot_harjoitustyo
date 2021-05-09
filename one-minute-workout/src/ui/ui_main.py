from tkinter import Tk, ttk, messagebox
from ui.ui_user_signup import UIUserSignup
from ui.ui_user_login import UIUserLogin
# from ui.ui_exercise import UIExercise


class UIMain:
    def __init__(self, root):
        self.root = root
        self.signup_frame = None
        self.login_frame = None
        self.quit_frame = None

    def start(self):

        self.signup_frame = ttk.Frame(master=self.root)
        self.signup_frame.pack()

        signup_label = ttk.Label(
            master=self.signup_frame, text="I'm a new user", font=("Helvetica", 12))
        signup_button = ttk.Button(master=self.signup_frame, text="Sign up",
                                   command=self.signup)

        signup_label.pack(pady=10)
        signup_button.pack()

        self.login_frame = ttk.Frame(master=self.root)
        self.login_frame.pack()

        login_label = ttk.Label(master=self.login_frame,
                                text="I already have an account", font=("Helvetica", 12))
        login_button = ttk.Button(master=self.login_frame, text="Log in",
                                  command=self.login)

        login_label.pack(pady=10)
        login_button.pack()

        self.quit_frame = ttk.Frame(master=self.root)
        self.quit_frame.pack()

        quit_label = ttk.Label(master=self.quit_frame,
                                text="Exit the app", font=("Helvetica", 12))
        quit_button = ttk.Button(master=self.quit_frame, text="Quit",
                                  command=self.root.destroy)

        quit_label.pack(pady=10)
        quit_button.pack()

        

        # self.exercise_frame = ttk.Frame(master=self.root)
        # self.exercise_frame.pack()

        # exercise_button = ttk.Button(master=self.login_frame, text="Check",
        #                           command=self.button_click_exercise)

        # exercise_button.pack()

    def signup(self):
        signup = UIUserSignup(self.root)
        self.signup_frame.destroy()
        self.login_frame.destroy()
        self.quit_frame.destroy()
        signup.start()

    def login(self):
        login = UIUserLogin(self.root)
        self.signup_frame.destroy()
        self.login_frame.destroy()
        self.quit_frame.destroy()
        login.start()

    # def button_click_exercise(self):
    #     exercise = UIExercise(self.root)
    #     self.signup_frame.destroy()
    #     self.login_frame.destroy()
    #     exercise.start()
