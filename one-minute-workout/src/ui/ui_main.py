from tkinter import Tk, ttk, messagebox
from ui.ui_user_signup import UIUserSignup
from ui.ui_user_login import UIUserLogin
# from ui.ui_exercise import UIExercise


class UIMain:
    def __init__(self, root):
        self.root = root
        self.signup_frame = None
        self.login_frame = None
        self.timer_frame = None

    def start(self):

        self.signup_frame = ttk.Frame(master=self.root)
        self.signup_frame.pack()

        signup_label = ttk.Label(
            master=self.signup_frame, text="I'm a new user")
        signup_button = ttk.Button(master=self.signup_frame, text="Sign up",
                                   command=self.button_click_signup)

        signup_label.pack()
        signup_button.pack()

        self.login_frame = ttk.Frame(master=self.root)
        self.login_frame.pack()

        login_label = ttk.Label(master=self.login_frame,
                                text="I already have an account")
        login_button = ttk.Button(master=self.login_frame, text="Log in",
                                  command=self.button_click_login)

        login_label.pack()
        login_button.pack()

        # self.exercise_frame = ttk.Frame(master=self.root)
        # self.exercise_frame.pack()

    
        # exercise_button = ttk.Button(master=self.login_frame, text="Check",
        #                           command=self.button_click_exercise)

        # exercise_button.pack()

    def button_click_signup(self):
        signup = UIUserSignup(self.root)
        self.signup_frame.destroy()
        self.login_frame.destroy()
        signup.start()

    def button_click_login(self):
        login = UIUserLogin(self.root)
        self.signup_frame.destroy()
        self.login_frame.destroy()
        login.start()

    # def button_click_exercise(self):
    #     exercise = UIExercise(self.root)
    #     self.signup_frame.destroy()
    #     self.login_frame.destroy()
    #     exercise.start()
