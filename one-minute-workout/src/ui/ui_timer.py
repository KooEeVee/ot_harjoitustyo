from tkinter import ttk, messagebox
from user import User
from timer import Timer
from counter import Counter
from ui.ui_exercise import UIExercise


class UITimer:
    """Class for user timer UI.

    Attributes:
        root: Tk() main window defined in the application class
        username: logged in user's username string
    """

    def __init__(self, root, username):
        """Class constructor to create user timer UI.

        Args:
            root: Tk() main window defined in the application class
            username: logged in user's username string
            user: User class object to get saved timer data related to logged in username
            user_timer_label: label for showing user's saved timer values string
            timer_stop_hours: entry for user's timer end value hours string
            timer_stop_minutes: entry for user's timer end value minutes string
            timer_interval: entry for user's timer interval minutes string
            timer_frame: frame for timer values showing related widgets
            set_timer_frame: frame for timer values setting related widgets
            exercise_frame: frame for exercise starting related widgets
            status_frame: frame for application status showing related widgets
            quit_frame: frame for application exit related widgets
        """
        self.root = root
        self.username = username
        self.user = User(self.username, "")
        self.user_timer_label = None
        self.timer_stop_hours = None
        self.timer_stop_minutes = None
        self.timer_interval = None
        self.timer_frame = None
        self.set_timer_frame = None
        self.exercise_frame = None
        self.status_frame = None
        self.quit_frame = None

    def start(self):
        """Start and define the user timer UI

        Show user timer. Saved values if user already has timer values set, else zero values.

        Entries for timer hours, minutes and interval.

        Apply timer and cancel timer buttons, start the exercise button and quit the app button.
        """
        self.timer_frame = ttk.Frame(master=self.root)
        self.timer_frame.pack()

        timer_label = ttk.Label(master=self.timer_frame,
                                text="Here's your timer:", font=("Helvetica", 12))
        self.user_timer_label = ttk.Label(master=self.timer_frame)
        self.user_timer_label.config(
            text=self.user.get_timer_json(), font=("Helvetica", 16))

        timer_label.pack(pady=10)
        self.user_timer_label.pack()

        self.set_timer_frame = ttk.Frame(master=self.root)
        self.set_timer_frame.pack()

        edit_label = ttk.Label(
            master=self.set_timer_frame, text="Edit your exercise timer", font=("Helvetica", 12))

        edit_label.pack(pady=10)

        stop_label_h = ttk.Label(
            master=self.set_timer_frame, text="My exercise time stops at (hours 00-23, two digits eg. 15): ", font=("Helvetica", 10))
        self.timer_stop_hours = ttk.Entry(master=self.set_timer_frame)
        stop_label_m = ttk.Label(
            master=self.set_timer_frame, text="My exercise time stops at (minutes 00-59, two digits eg. 05): ", font=("Helvetica", 10))
        self.timer_stop_minutes = ttk.Entry(master=self.set_timer_frame)
        interval_label = ttk.Label(
            master=self.set_timer_frame, text="My exercise frequency is (minutes 1-180): ", font=("Helvetica", 10))
        self.timer_interval = ttk.Entry(master=self.set_timer_frame)

        stop_label_h.pack()
        self.timer_stop_hours.pack()
        stop_label_m.pack()
        self.timer_stop_minutes.pack()
        interval_label.pack()
        self.timer_interval.pack()

        apply_button = ttk.Button(master=self.set_timer_frame, text="Apply timer",
                                  command=self._apply_timer)

        cancel_button = ttk.Button(master=self.set_timer_frame, text="Cancel",
                                   command=self._cancel)

        apply_button.pack(pady=10)
        cancel_button.pack(pady=10)

        self.status_frame = ttk.Frame(master=self.root)
        self.status_frame.pack()

        self.exercise_frame = ttk.Frame(master=self.root)
        self.exercise_frame.pack()

        exercise_label = ttk.Label(master=self.exercise_frame,
                                   text="Start the One-Minute Workout", font=("Helvetica", 16))
        exercise_button = ttk.Button(master=self.exercise_frame, text="Start exercise",
                                     command=self._start_exercise)

        exercise_label.pack(pady=20)
        exercise_button.pack()

        self.quit_frame = ttk.Frame(master=self.root)
        self.quit_frame.pack()

        quit_button = ttk.Button(master=self.quit_frame, text="Quit the app",
                                 command=self.root.destroy)

        quit_button.pack(pady=50)

    def _apply_timer(self):
        """Save timer values, end time and interval, with the user data in the users.json file.

        Check that the entries are digits, stop hours and minutes entries' length is 2 and interval entry length is greater than 0. 
        Check that stop value hours is not negative and less than 24.
        Check that stop value minutes is not negative and less than 60.
        Check that inteval value is not negative or 0 and less than 181.
        """
        stop_value_h = self.timer_stop_hours.get()
        stop_value_m = self.timer_stop_minutes.get()
        interval_value = self.timer_interval.get()
        stop_value = f"{self.timer_stop_hours.get()}:{self.timer_stop_minutes.get()}"
        # user_value = self.username
        # timer_start = f"{self.timer_start_hours.get()}:{self.timer_start_minutes.get()}"
        # timer_stop = f"{self.timer_stop_hours.get()}:{self.timer_stop_minutes.get()}"
        timer = Timer(stop_value, interval_value, self.username)

        # if start_value_h.isdigit() and len(start_value_h) == 2 and int(start_value_h) >= 0 and int(start_value_h) < 24:
        #     if start_value_m.isdigit() and len(start_value_m) == 2 and int(start_value_m) >= 0 and int(start_value_m) < 60:
        if stop_value_h.isdigit() and len(stop_value_h) == 2 and int(stop_value_h) >= 0 and int(stop_value_h) < 24:
            if stop_value_m.isdigit() and len(stop_value_m) == 2 and int(stop_value_m) >= 0 and int(stop_value_m) < 60:
                # if datetime.time(int(start_value_h), int(start_value_m)) < datetime.time(int(stop_value_h), int(stop_value_m)):
                if interval_value.isdigit() and len(interval_value) > 0 and int(interval_value) > 0 and int(interval_value) < 181:
                    timer.save_timer_to_user()
                    # goodbye = ttk.Label(
                    #     master=self.root, text="Timer is ready, thank you!")
                    # goodbye.pack()
                    # self.timer_start_hours.delete(0, "end")
                    # self.timer_start_minutes.delete(0, "end")
                    self.timer_stop_hours.delete(0, "end")
                    self.timer_stop_minutes.delete(0, "end")
                    self.timer_interval.delete(0, "end")
                    # timer_label = ttk.Label(
                    #     master=self.root, text="Here's your timer:", font=("Helvetica", 12))
                    # user_timer_label = ttk.Label(master=self.root)
                    self.user_timer_label.config(
                        text=self.user.get_timer_json(), font=("Helvetica", 16))
                    # timer_label.pack(pady=10)
                    # user_timer_label.pack()

                else:
                    messagebox.showinfo(
                        "Check the interval minutes", "Please try again")
                    self.timer_interval.delete(0, "end")
                # else:
                #     messagebox.showinfo(
                #         "Start time must be before stop time", "Please try again")
                #     self.timer_stop_hours.delete(0, "end")
                #     self.timer_stop_minutes.delete(0, "end")
            else:
                messagebox.showinfo(
                    "Check the stopping minutes", "Please try again")
                self.timer_stop_minutes.delete(0, "end")
        else:
            messagebox.showinfo(
                "Check the stopping hours", "Please try again")
            self.timer_stop_hours.delete(0, "end")
        #     else:
        #         messagebox.showinfo(
        #             "Check the starting minutes", "Please try again")
        #         self.timer_start_minutes.delete(0, "end")
        # else:
        #     messagebox.showinfo("Check the starting hours", "Please try again")
        #     self.timer_start_hours.delete(0, "end")

    def _cancel(self):
        """Clear the timer UI entries"""
        # self.timer_start_hours.delete(0, "end")
        # self.timer_start_minutes.delete(0, "end")
        self.timer_stop_hours.delete(0, "end")
        self.timer_stop_minutes.delete(0, "end")
        self.timer_interval.delete(0, "end")

    def _start_exercise(self):
        """Start the workout schedule.

        Check that the timer values are set.

        Create a Counter class object to count the amount of exercise loops in the schedule and initialize the exercise loop with the user's timer interval.
        """
        
        if int(self.user.get_timer_interval()) > 0:
            self.set_timer_frame.destroy()
            self.exercise_frame.destroy()
            self.root.iconify()
            stop_value = self.user.get_timer_stop()
            interval_value = self.user.get_timer_interval()
            counter = Counter(stop_value, interval_value)
            loops, interval_s = counter.count_exercise_loops()
            # ttimer_label = ttk.Label(
            #     master=self.status_frame, text=f"Exercises remaining: {int(loops)}", font=("Helvetica", 12))
            # ttimer_label.pack(pady=10)
            for i in range(int(loops)):
                self.root.after(i*interval_s*1000, self._open_exercise_window)
        else:
            messagebox.showinfo(
                    "Timer values are empty", "Please try again")

    def _open_exercise_window(self):
        "Start a new exercise UI"
        exercise = UIExercise(self.root)
        exercise.start()