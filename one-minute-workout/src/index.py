from tkinter import Tk
from ui.ui_user_login import UIUserLogin
from ui.ui_user_signup import UIUserSignup
from ui.ui_main import UIMain
import csv
from user import User

def main():

    # user = User("kaisanen", "test")
    # user.new_user_csv()
    # print(user.get_username_csv("kaisanen"))
    # print(user.get_password_csv("kaisanen"))

    mainscreen = Tk()
    mainscreen.title("Sign up or log in to One-Minute Workout")
    mainscreen.geometry("1000x500")
    ui = UIMain(mainscreen)
    ui.start()
    mainscreen.mainloop()

    # signup = Tk()
    # signup.title("Sign up to One-Minute Workout")
    # signup.geometry("400x150")
    # ui = UIUserSignup(signup)
    # ui.start()
    # signup.mainloop()

    # login = Tk()
    # login.title("Log in to One-Minute Workout")
    # login.geometry("400x150")
    # ui = UIUserLogin(login)
    # ui.start()
    # login.mainloop()

    """ db = Database(DATABASE_ENDPOINT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME)
    db.connect_db()
    print(db.select_user("testi2"))
    db.disconnect_db() """


if __name__ == "__main__":
    main()
