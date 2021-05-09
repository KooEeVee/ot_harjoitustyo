from datetime import datetime, timedelta

class Counter:
    def __init__(self, end, interval):
        self.end_time = end
        self.interval = interval

    def count_exercise_loops(self):
        now = datetime.now()
        tomorrow = now + timedelta(days=1)
        print(now)
        print(tomorrow)
        current_date = now.strftime("%Y-%m-%d")
        tomorrow_date = tomorrow.strftime("%Y-%m-%d")
        end_time_string = f"{current_date} {self.end_time}:00"
        end_time_object = datetime.strptime(end_time_string, "%Y-%m-%d %H:%M:%S")

        print(end_time_object)
        print(end_time_object)
        if end_time_object < now:
            end_time_string = f"{tomorrow_date} {self.end_time}:00"
            end_time_object = datetime.strptime(end_time_string, "%Y-%m-%d %H:%M:%S")
            print(end_time_object)
            exercise_time = end_time_object - now
            print(exercise_time)
            exercise_time_s = exercise_time.total_seconds()
            print(exercise_time_s)
        else:
            exercise_time = end_time_object - now
            print(exercise_time)
            exercise_time_s = exercise_time.total_seconds()
            print(exercise_time_s)
        interval_s = int(self.interval) * 60
        loops = exercise_time_s // interval_s
        return loops
