from tkinter import Tk
from ui.ui_main import UIMain
from user import User
from application import Application
import json

def main():

    # app = Application()
    # app.initialize_json()
    user = User("niilo", "1111")
    # user.new_user_json()
    print(user.get_user_json())
    print(user.get_password_json("niilo"))
    

    # mainscreen = Tk()
    # mainscreen.title("Sign up or log in to One-Minute Workout")
    # mainscreen.geometry("1000x500")
    # ui = UIMain(mainscreen)
    # ui.start()
    # mainscreen.mainloop()

if __name__ == "__main__":
    main()
