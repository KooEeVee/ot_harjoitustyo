from tkinter import ttk
from PIL import Image, ImageTk
from user import User
from exercise import Exercise

class UIExercise:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.user = User(self.username, "")
        self.number = "1"
        self.exercise = Exercise("1")

    def start(self):
        text_label = ttk.Label(master=self.root)
        text_label.config(text=self.exercise.get_exercise_text())
        image_file = f'src/exercises/{self.number}.png'
        image = Image.open(image_file)
        render = ImageTk.PhotoImage(image)
        image_label = ttk.Label(master=self.root, image=render)
        image_label.image = render
        countdown_label = ttk.Label(master=self.root)
        #countdown_label.config(pass)

        text_label.pack()
        image_label.pack()
        countdown_label.pack()
