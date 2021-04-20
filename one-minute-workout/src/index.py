from tkinter import Tk
from ui.ui_main import UIMain

def main():
    mainscreen = Tk()
    mainscreen.title("Sign up or log in to One-Minute Workout")
    mainscreen.geometry("400x150")
    ui = UIMain(mainscreen)
    ui.start()
    mainscreen.mainloop()

if __name__ == "__main__":
    main()
