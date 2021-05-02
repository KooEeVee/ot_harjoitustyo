from tkinter import ttk, Toplevel
from PIL import Image, ImageTk
from user import User
from exercise import Exercise

class UIExercise:
    def __init__(self, root, username):
        self.root = root
        self.top = Toplevel()
        self.username = username
        self.user = User(self.username, "")
        self.number = "1"
        self.exercise = Exercise("1")

    def start(self):
        self.top.geometry("400x400")
        self.top.title("Exercise")
        text_label = ttk.Label(master=self.top)
        text_label.config(text=self.exercise.get_exercise_text())
        image_file = f'src/exercises/{self.number}.png'
        image = Image.open(image_file)
        render = ImageTk.PhotoImage(image)
        image_label = ttk.Label(master=self.top, image=render)
        image_label.image = render
        # countdown_label = ttk.Label(master=self.top)
        #countdown_label.config(pass)

        text_label.pack()
        image_label.pack()
        # countdown_label.pack()
        self.top.mainloop()
