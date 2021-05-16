import random
from tkinter import ttk, Toplevel
from PIL import Image, ImageTk
from exercise import Exercise


class UIExercise:
    """Class for exercise UI.

    Attributes:
        root: Tk() main window defined in the application class
    """

    def __init__(self, root):
        """Class constructor to create exercise UI.

        Args:
            root: Tk() main window defined in the application class
            top: Toplevel() new window for the exercise UI
            number: random integer from 1 to 5
            exercise: random Exercise object
            text_frame: frame for exercise text related widgets
            image_frame: frame for exercise image related widgets
        """
        self.root = root
        self.top = Toplevel()
        self.top.geometry(
            f"400x300+{self.top.winfo_screenwidth()}+{self.top.winfo_screenheight()}")
        self.top.title("Exercise")
        self.number = random.randint(1, 5)
        self.exercise = Exercise(self.number)
        self.text_frame = None
        self.image_frame = None

    def start(self):
        """Start and define the exercise UI.

        Exercise text, 60 second progressbar and exercise image.

        Exercise window closes after 60 seconds.
        """
        self.text_frame = ttk.Frame(master=self.top)
        self.text_frame.pack()

        text_label = ttk.Label(master=self.text_frame, font=("Helvetica", 12))
        text_label.config(text=self.exercise.get_exercise_text())
        text_label.pack()

        progress_bar = ttk.Progressbar(
            master=self.text_frame, orient="horizontal", length=200, mode="determinate", maximum=60)
        progress_bar.pack(pady=10)
        progress_bar.start(interval=1000)

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
