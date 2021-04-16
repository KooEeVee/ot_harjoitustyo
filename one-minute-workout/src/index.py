import csv
from tkinter import Tk, ttk
from user import User
from ui_user_signup import UIUserSignup


def main():
    signup = Tk()
    signup.title("Sign up to One-Minute Workout")
    signup.geometry("400x150")
    ui = UIUserSignup(signup)
    ui.start()
    signup.mainloop()


if __name__ == "__main__":
    main()
