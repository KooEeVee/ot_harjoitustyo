import json
from os import path
from tkinter import Tk
from ui.ui_main import UIMain


class Application:
    def __init__(self):
        self.mainscreen = Tk()

    def initialize_users_json(self):
        if path.getsize("src/users.json") == 0:
            data = {}
            data["users"] = []
            with open("src/users.json", "w") as f:
                json.dump(data, f, indent=4)
        else:
            pass

    # def initialize_exercise_json(self):
    #     if path.getsize("src/exercises.json") == 0:
    #         data = {}
    #         data["exercises"] = []
    #         with open("src/exercises.json", "w") as f:
    #             json.dump(data, f, indent=4)
    #     else:
    #         pass

    def initialize_ui(self):
        mainscreen = self.mainscreen
        mainscreen.title("Welcome to One-Minute Workout")
        mainscreen_w = 500
        mainscreen_h = 600
        screen_w = mainscreen.winfo_screenwidth()
        screen_h = mainscreen.winfo_screenheight()
        mainscreen.geometry(
            f"{mainscreen_w}x{mainscreen_h}+{screen_w}+{screen_h}")
        ui_main = UIMain(mainscreen)
        ui_main.start()
        mainscreen.mainloop()

    def close_ui(self):
        self.mainscreen.destroy()
