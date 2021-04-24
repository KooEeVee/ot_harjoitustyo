import datetime
from tkinter import ttk, messagebox
from timer import Timer
from user import User

class UITimer:
    def __init__(self, root):
        self.root = root
        self.timer_start_hours = None
        self.timer_start_minutes = None
        self.timer_stop_hours = None
        self.timer_stop_minutes = None
        self.timer_interval = None
        self.user = None


    def start(self):
        user_label = ttk.Label(master=self.root, text="My username: ")
        self.user = ttk.Entry(master=self.root)
        self.timer_start_hours = ttk.Entry(master=self.root)
        start_label_h = ttk.Label(master=self.root, text="My exercise time starts at (hours): ")
        self.timer_start_hours = ttk.Entry(master=self.root)
        start_label_m = ttk.Label(master=self.root, text="My exercise time starts at (minutes): ")
        self.timer_start_minutes = ttk.Entry(master=self.root)
        stop_label_h = ttk.Label(master=self.root, text="My exercise time stops at (hours): ")
        self.timer_stop_hours = ttk.Entry(master=self.root)
        stop_label_m = ttk.Label(master=self.root, text="My exercise time stops at (minutes): ")
        self.timer_stop_minutes = ttk.Entry(master=self.root)
        interval_label = ttk.Label(master=self.root, text="My exercise frequency is (minutes): ")
        self.timer_interval = ttk.Entry(master=self.root)
        button_apply = ttk.Button(master=self.root, text="Apply",
                            command=self.button_click_to_apply_timer)

        button_cancel = ttk.Button(master=self.root, text="Cancel",
                            command=self.button_click_to_cancel_timer)

        user_label.pack()
        self.user.pack()
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
        user_value = self.user.get()
        user = User(user_value, "")
        timer = Timer(start_value_h, start_value_m, stop_value_h, stop_value_m, interval_value, user_value)
        if not user.get_user_json():
            messagebox.showinfo("User not found", "Please try again")
            self.user.delete(0, "end")
        else:
            if start_value_h.isdigit() and len(start_value_h) > 0:
                if start_value_m.isdigit() and len(start_value_m) > 0:
                    if stop_value_h.isdigit() and len(stop_value_h) > 0:
                        if stop_value_m.isdigit() and len(stop_value_m) > 0:
                            if interval_value.isdigit() and len(interval_value) > 0:
                                timer.save_timer_to_user()
                                goodbye = ttk.Label(master=self.root, text="Timer is ready, thank you!")
                                goodbye.pack()
                                self.timer_start_hours.delete(0, "end")
                                self.timer_start_minutes.delete(0, "end")
                                self.timer_stop_hours.delete(0, "end")
                                self.timer_stop_minutes.delete(0, "end")
                                self.timer_interval.delete(0, "end")
                            else:
                                messagebox.showinfo("Check the interval minutes", "Please try again")
                                self.timer_interval.delete(0, "end")
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
        self.user.delete(0, "end")
        self.timer_start_hours.delete(0, "end")
        self.timer_start_minutes.delete(0, "end")
        self.timer_stop_hours.delete(0, "end")
        self.timer_stop_minutes.delete(0, "end")
        self.timer_interval.delete(0, "end")
