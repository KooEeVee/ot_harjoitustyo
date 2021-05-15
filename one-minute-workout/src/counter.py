from datetime import datetime, timedelta


class Counter:
    """Class to handle time and date related tasks.

    Define date today, date tomorrow and user's timer end time as datetime objects and workout schedule lenght in seconds.
    Define user's timer interval in seconds and count exercise loops by dividing workout length with timer interval.

    Attributes:
        end: user's timer end time string
        interval: user's timer interval string
    """

    def __init__(self, end, interval):
        """Class constructor to create a counter.

        Args:
            end: user's timer end time string
            interval: user's timer interval string
            now: current date and time datetime object
        """
        self.end_time = end
        self.interval = interval
        self.now = datetime.now()

    def count_exercise_loops(self):
        """Count the amount of exercise loops by dividing user's workout schedule length with timer interval.

        Notice the 24 hours time cycle, if workout schedule ends during the same day or tomorrow.

        Returns:
            A tuple containing values for the amount of exercise loops (float) and timer interval in seconds (int)
        """
        tomorrow = self.now + timedelta(days=1)
        current_date = self.now.strftime("%Y-%m-%d")
        tomorrow_date = tomorrow.strftime("%Y-%m-%d")
        end_time_string = f"{current_date} {self.end_time}:00"
        end_time_object = datetime.strptime(
            end_time_string, "%Y-%m-%d %H:%M:%S")

        if end_time_object < self.now:
            end_time_string = f"{tomorrow_date} {self.end_time}:00"
            end_time_object = datetime.strptime(
                end_time_string, "%Y-%m-%d %H:%M:%S")
            exercise_time = end_time_object - self.now
            exercise_time_s = exercise_time.total_seconds()
        else:
            exercise_time = end_time_object - self.now
            exercise_time_s = exercise_time.total_seconds()
        interval_s = int(self.interval) * 60
        loops = exercise_time_s // interval_s
        return (loops, interval_s)
