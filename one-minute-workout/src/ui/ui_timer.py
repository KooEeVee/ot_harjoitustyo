import datetime
from tkinter import ttk, messagebox
from timer import Timer
from user import User

class UITimer:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.user = User(self.username, "")
        self.timer_start_hours = None
        self.timer_start_minutes = None
        self.timer_stop_hours = None
        self.timer_stop_minutes = None
        self.timer_interval = None

    def start(self):
        timer_label = ttk.Label(master=self.root, text="Here's your timer:")
        user_timer_label = ttk.Label(master=self.root)
        user_timer_label.config(text=self.user.get_timer_json())
        welcome_label = ttk.Label(master=self.root, text="Set or edit your exercise timer")
        self.timer_start_hours = ttk.Entry(master=self.root)
        start_label_h = ttk.Label(master=self.root, text="My exercise time starts at (hours, two digits eg. 07): ")
        self.timer_start_hours = ttk.Entry(master=self.root)
        start_label_m = ttk.Label(master=self.root, text="My exercise time starts at (minutes, two digits eg. 20): ")
        self.timer_start_minutes = ttk.Entry(master=self.root)
        stop_label_h = ttk.Label(master=self.root, text="My exercise time stops at (hours, two digits eg. 15): ")
        self.timer_stop_hours = ttk.Entry(master=self.root)
        stop_label_m = ttk.Label(master=self.root, text="My exercise time stops at (minutes, two digits eg. 05): ")
        self.timer_stop_minutes = ttk.Entry(master=self.root)
        interval_label = ttk.Label(master=self.root, text="My exercise frequency is (minutes): ")
        self.timer_interval = ttk.Entry(master=self.root)
        button_apply = ttk.Button(master=self.root, text="Apply",
                            command=self.button_click_to_apply_timer)

        button_cancel = ttk.Button(master=self.root, text="Cancel",
                            command=self.button_click_to_cancel_timer)

        timer_label.pack()
        user_timer_label.pack()
        welcome_label.pack()
        start_label_h.pack()
        self.timer_start_hours.pack()
        start_label_m.pack()
        self.timer_start_minutes.pack()
        stop_label_h.pack()
        self.timer_stop_hours.pack()
        stop_label_m.pack()
        self.timer_stop_minutes.pack()
        interval_label.pack()
        self.timer_interval.pack()
        button_apply.pack()
        button_cancel.pack()

    def button_click_to_apply_timer(self):
        start_value_h = self.timer_start_hours.get()
        start_value_m = self.timer_start_minutes.get()
        stop_value_h = self.timer_stop_hours.get()
        stop_value_m = self.timer_stop_minutes.get()
        interval_value = self.timer_interval.get()
        user_value = self.username
        timer_start = f"{self.timer_start_hours.get()}:{self.timer_start_minutes.get()}"
        timer_stop = f"{self.timer_stop_hours.get()}:{self.timer_stop_minutes.get()}"
        timer = Timer(timer_start, timer_stop, interval_value, user_value)
        
        if start_value_h.isdigit() and len(start_value_h) == 2 and int(start_value_h) > 0 and int(start_value_h) < 24:
            if start_value_m.isdigit() and len(start_value_m) ==2 and int(start_value_m) > 0 and int(start_value_m) < 60:
                if stop_value_h.isdigit() and len(stop_value_h) ==2 and int(stop_value_h) > 0 and int(stop_value_h) < 24:
                    if stop_value_m.isdigit() and len(stop_value_m) ==2 and int(stop_value_m) > 0 and int(stop_value_m) < 60:
                        if datetime.time(int(start_value_h), int(start_value_m)) < datetime.time(int(stop_value_h), int(stop_value_m)):
                            if interval_value.isdigit() and len(interval_value) > 0:
                                timer.save_timer_to_user()
                                goodbye = ttk.Label(master=self.root, text="Timer is ready, thank you!")
                                goodbye.pack()
                                self.timer_start_hours.delete(0, "end")
                                self.timer_start_minutes.delete(0, "end")
                                self.timer_stop_hours.delete(0, "end")
                                self.timer_stop_minutes.delete(0, "end")
                                self.timer_interval.delete(0, "end")
                                timer_label = ttk.Label(master=self.root, text="Here's your timer:")
                                user_timer_label = ttk.Label(master=self.root)
                                user_timer_label.config(text=self.user.get_timer_json())
                                timer_label.pack()
                                user_timer_label.pack()

                            else:
                                messagebox.showinfo("Check the interval minutes", "Please try again")
                                self.timer_interval.delete(0, "end")
                        else:
                            messagebox.showinfo("Start time must be before stop time", "Please try again")
                            self.timer_stop_hours.delete(0, "end")
                            self.timer_stop_minutes.delete(0, "end")
                    else:
                        messagebox.showinfo("Check the stopping minutes", "Please try again")
                        self.timer_stop_minutes.delete(0, "end")
                else:
                    messagebox.showinfo("Check the stopping hours", "Please try again")
                    self.timer_stop_hours.delete(0, "end")
            else:
                messagebox.showinfo("Check the starting minutes", "Please try again")
                self.timer_start_minutes.delete(0, "end")
        else:
            messagebox.showinfo("Check the starting hours", "Please try again")
            self.timer_start_hours.delete(0, "end")
        
    def button_click_to_cancel_timer(self):
        self.timer_start_hours.delete(0, "end")
        self.timer_start_minutes.delete(0, "end")
        self.timer_stop_hours.delete(0, "end")
        self.timer_stop_minutes.delete(0, "end")
        self.timer_interval.delete(0, "end")
