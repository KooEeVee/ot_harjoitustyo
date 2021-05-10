import random
from tkinter import ttk, Toplevel
from PIL import Image, ImageTk
from exercise import Exercise

class UIExercise:
    def __init__(self, root):
        self.root = root
        self.top = Toplevel()
        self.top.geometry(
            f"400x300+{self.top.winfo_screenwidth()}+{self.top.winfo_screenheight()}")
        self.top.title("Exercise")
        self.number = random.randint(1, 5)
        self.exercise = Exercise(self.number)
        # self.end = end
        # self.interval = interval
        self.text_frame = None
        self.image_frame = None

    def start(self):
        self.text_frame = ttk.Frame(master=self.top)
        self.text_frame.pack()

        text_label = ttk.Label(master=self.text_frame, font=("Helvetica", 12))
        text_label.config(text=self.exercise.get_exercise_text())
        text_label.pack(pady=20)

        self.image_frame = ttk.Frame(master=self.top)
        self.image_frame.pack()
        image_file = f'src/exercises/{self.number}.jpg'
        global image
        image = Image.open(image_file)
        render = ImageTk.PhotoImage(image)
        image_label = ttk.Label(master=self.image_frame, image=render)
        image.image = render
        image_label.pack()
        
        self.top.after(60000, self.top.destroy)
   
