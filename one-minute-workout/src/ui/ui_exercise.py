import random
from tkinter import ttk, Toplevel
from PIL import Image, ImageTk
from exercise import Exercise

class UIExercise:
    def __init__(self, root):
        self.root = root
        self.number = random.randint(1, 5)
        self.top = Toplevel()
        self.top.geometry("600x400")
        self.top.title("Exercise")
        self.exercise = Exercise(self.number)

    def start(self):
        text_label = ttk.Label(master=self.top)
        text_label.config(text=self.exercise.get_exercise_text())
        image_file = f'src/exercises/{self.number}.png'
        image = Image.open(image_file)
        render = ImageTk.PhotoImage(image)
        image_label = ttk.Label(master=self.top, image=render)
        image_label.image = render

        text_label.pack()
        image_label.pack()

        self.top.after(60000, self.top.destroy)