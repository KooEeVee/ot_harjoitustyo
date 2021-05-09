from application import Application
from counter import Counter
from ui.ui_exercise import UIExercise
from tkinter import Tk


def main():

    app = Application()
    app.initialize_users_json()
    app.initialize_ui()


if __name__ == "__main__":
    main()
