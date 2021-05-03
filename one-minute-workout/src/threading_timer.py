# from datetime import datetime
# import time
# from user import User
# from exercise import Exercise
# from ui.ui_exercise import UIExercise

# class ThreadingTimer:
#     def __init__(self, username):
#         self.timer_start = None
#         self.timer_stop = None
#         self.interval = None
#         self.username = username
#         self.number = None
#         self.user = User(self.username, "")

#     def exercise_wait_time(self):
#         now = datetime.now()
#         user_start_time_string = f"{now.year} {now.month} {now.day} {self.user.get_timer_start()}"
#         user_start_time = datetime.strptime(user_start_time_string, "%Y %m %d %H:%M")
#         user_wait_time = user_start_time - now
#         return user_wait_time

#     def exercise_interval_time(self):
#         self.interval = self.user.get_timer_interval()
#         return self.interval

