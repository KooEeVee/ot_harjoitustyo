import json
from os import path
from tkinter import Tk
from ui.ui_main import UIMain

class Application:
    def __init__(self):
        self.test = None

    def initialize_json(self):
        if path.getsize("src/users.json") == 0:
            data = {}
            data["users"] = []
            with open ("src/users.json", "w") as f:
                json.dump(data, f, indent=4)
        else:
            pass
    
    def initialize_ui(self):
        mainscreen = Tk()
        mainscreen.title("Sign up or log in to One-Minute Workout")
        mainscreen.geometry("1000x500")
        ui = UIMain(mainscreen)
        ui.start()
        mainscreen.mainloop()
