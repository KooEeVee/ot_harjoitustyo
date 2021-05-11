from datetime import datetime, timedelta

class Counter:
    """Class to handle time and date related tasks.

    Attributes:
        end (String): user's timer end time
        interval (String): user's timer interval
    """
    def __init__(self, end, interval):
        """Class constructor to create new counter.

        Args:
            end (String): user's timer end time
            interval (String): user's timer interval
        """
        self.end_time = end
        self.interval = interval

    def count_exercise_loops(self):
        """Count the amount of exercise loops based on user's timer end and interval.

        Returns:
            ((float), (int)): a tuple containing values for the amount of exercise loops and timer interval in seconds
        """
        now = datetime.now()
        tomorrow = now + timedelta(days=1)
        current_date = now.strftime("%Y-%m-%d")
        tomorrow_date = tomorrow.strftime("%Y-%m-%d")
        end_time_string = f"{current_date} {self.end_time}:00"
        end_time_object = datetime.strptime(
            end_time_string, "%Y-%m-%d %H:%M:%S")

        if end_time_object < now:
            end_time_string = f"{tomorrow_date} {self.end_time}:00"
            end_time_object = datetime.strptime(
                end_time_string, "%Y-%m-%d %H:%M:%S")
            exercise_time = end_time_object - now
            exercise_time_s = exercise_time.total_seconds()
        else:
            exercise_time = end_time_object - now
            exercise_time_s = exercise_time.total_seconds()
        interval_s = int(self.interval) * 60
        loops = exercise_time_s // interval_s
        return (loops, interval_s)
