from tkinter import ttk, StringVar
from user import User


class UIExercise:
    def __init__(self, root):
        self.root = root
        self.user = User("kaisa", "")

    def start(self):
        welcome_label = ttk.Label(master=self.root, text="Here's your timer")
        timer_label = ttk.Label(master=self.root)
        timer_label.config(text=self.user.get_timer_json())

        welcome_label.pack()
        timer_label.pack()
