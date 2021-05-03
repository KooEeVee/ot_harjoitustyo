# import random
# import threading
# import time
# import datetime
# from tkinter import ttk, Toplevel
# from user import User
# from threading_timer import ThreadingTimer
# from ui.ui_exercise import UIExercise

# class UIThreadingTimer:
#     def __init__(self, root, username):
#         self.root = root
#         self.top = Toplevel()
#         self.top.geometry("600x400")
#         self.top.title("Exercise")
#         self.username = username
#         self.user = User(self.username, "")
#         self.wait = None
#         self.interval = 10.0
#         self.number = random.randint(1, 5)

#     def initialize_exercise_ui(self):
#         exercise_ui = UIExercise(self.top, self.number)
#         exercise_ui.start()
#         # self.top.deiconify()
#         self.top.after(10000, self.top.destroy)

#     def counter(self, trigger):
#         while True:
#             time.sleep(1)
#             now = time.strftime("%H:%M:%S")
#             if now == trigger:
#                 self.initialize_exercise_ui()
#             break

#     def start(self):
#         self.counter("19:10:00")
#         #self.initialize_exercise_ui()
#         #self.initialize_exercise_ui()
#         # self.top.iconify()
#         #ttimer = ThreadingTimer(self.username)
#         #self.wait = ttimer.exercise_wait_time()
#         #wait_ms = int(self.wait.total_seconds()*1000)
#         #print(self.wait)
#         #print(wait_ms)
#         #self.interval = ttimer.exercise_interval_time()
#         #print(self.interval)
#         #timer_timer = threading.Timer(10.0, self.initialize_exercise_ui())
#         # timer_timer.start()
#         # self.top.after(3000, timer_timer.start())