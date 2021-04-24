from tkinter import ttk, messagebox
from timer import Timer

class UITimer:
    def __init__(self, root):
        self.root = root
        self.start = None
        self.stop = None
        self.interval = None

    def start(self):
        start_label = ttk.Label(master=self.root, text="My exercise time starts at: ")
        self.start = ttk.Entry(master=self.root)
        stop_label = ttk.Label(master=self.root, text="My exercise time stops at: ")
        self.stop = ttk.Entry(master=self.root)
        interval_label = ttk.Label(master=self.root, text="My exercise frequency is: ")
        self.interval = ttk.Entry(master=self.root)
        button_apply = ttk.Button(master=self.root, text="Apply",
                            command=self.button_click_to_apply_timer)

        button_cancel = ttk.Button(master=self.root, text="Cancel",
                            command=self.button_click_to_cancel_timer)

        start_label.pack()
        self.start.pack()
        stop_label.pack()
        self.stop.pack()
        interval_label.pack()
        self.interval.pack()
        button_apply.pack()
        button_cancel.pack()

    def button_click_to_apply_timer(self):
        start_value = self.start.get()
        stop_value = self.stop.get()
        interval_value = self.interval.get()
        timer = Timer(start_value, stop_value, interval_value)
        
    def button_click_to_cancel_timer(self):
        self.start.delete(0, "end")
        self.stop.delete(0, "end")
        self.interval.delete(0, "end")
