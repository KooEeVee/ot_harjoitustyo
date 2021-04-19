from tkinter import Tk
from ui_user_signup import UIUserSignup
from database import Database
from config import DATABASE_ENDPOINT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME

def main():
    signup = Tk()
    signup.title("Sign up to One-Minute Workout")
    signup.geometry("400x150")
    ui = UIUserSignup(signup)
    ui.start()
    signup.mainloop()

    """ db = Database(DATABASE_ENDPOINT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME)
    db.connect_db()
    print(db.select_user("testi2"))
    db.disconnect_db() """


if __name__ == "__main__":
    main()
