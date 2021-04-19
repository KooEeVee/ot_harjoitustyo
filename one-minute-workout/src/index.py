from tkinter import Tk
from ui.ui_user_login import UIUserLogin

def main():
    login = Tk()
    login.title("Log in to One-Minute Workout")
    login.geometry("400x150")
    ui = UIUserLogin(login)
    ui.start()
    login.mainloop()

    """ db = Database(DATABASE_ENDPOINT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME)
    db.connect_db()
    print(db.select_user("testi2"))
    db.disconnect_db() """


if __name__ == "__main__":
    main()
