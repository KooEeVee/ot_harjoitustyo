import json
from os import path
from tkinter import Tk
from ui.ui_main import UIMain


class Application:
    """Class for tasks needed before application launch."""
    def __init__(self):
        """Class constructor to create new application.

        Args:
            Tk(): tkinter main window
        """
        self.mainscreen = Tk()

    def initialize_users_json(self):
        """Initialize the users.json file if not available."""

        if path.getsize("src/db/users.json") == 0:
            data = {}
            data["users"] = []
            with open("src/db/users.json", "w") as f:
                json.dump(data, f, indent=4)
        else:
            pass

    def initialize_ui(self):
        """Initialize the application main window UI."""
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
