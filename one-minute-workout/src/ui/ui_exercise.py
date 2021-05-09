import random
import time
from tkinter import ttk, Toplevel
from PIL import Image, ImageTk
from exercise import Exercise
from counter import Counter


class UIExercise:
    def __init__(self, root, end, interval):
        self.root = root
        self.top = Toplevel()
        self.top.geometry("600x400")
        self.top.title("Exercise")
        self.number = random.randint(1, 5)
        self.exercise = Exercise(self.number)
        self.end = end
        self.interval = interval
        self.loops = 0

    def start(self):
        global exeimage
        
        text_label = ttk.Label(master=self.top)
        text_label.config(text=self.exercise.get_exercise_text())
        image_file = f'src/exercises/{self.number}.png'
        image = Image.open(image_file)
        resized_image = image.resize((600, 300), image.ANTIALIAS)
        exe_image = ImageTk.PhotoImage(resized_image)
        image_label = ttk.Label(master=self.top, image=exe_image)
    
        text_label.pack()
        image_label.pack()

        self.top.after(5000, self.top.destroy())