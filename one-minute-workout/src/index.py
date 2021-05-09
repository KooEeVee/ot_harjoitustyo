from application import Application
from counter import Counter
from ui.ui_exercise import UIExercise
from tkinter import Tk


def main():

    app = Application()
    app.initialize_users_json()
    app.initialize_ui()

    # counter = Counter("10:10", "2")
    # print(counter.count_exercise_loops())

    # mainscreen = Tk()
    # mainscreen.title("Welcome to One-Minute Workout")
    # mainscreen.geometry("1000x500")
    # exe = UIExercise(mainscreen, "19:00", "10")
    # exe.start()
    # mainscreen.mainloop()

if __name__ == "__main__":
    main()
