import json

class Timer:
    def __init__(self, start_h, start_m, stop_h, stop_m, interval, user):
        self.start_hours = start_h
        self.start_minutes = start_m
        self.stop_hours = stop_h
        self.stop_minutes = stop_m
        self.interval = interval
        self.user = user

    def save_timer_to_user(self):
        timer_start = f"{self.start_hours}:{self.start_minutes}"
        timer_stop = f"{self.start_minutes}:{self.stop_minutes}"
        timer_interval = f"{self.interval}"
        timer_user = self.user
        with open ("src/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user["username"] == timer_user:
                    user["timer_start"] = timer_start
                    user["timer_stop"] = timer_stop
                    user["timer_interval"] = timer_interval
    
        with open ("src/users.json", "w") as f:
            json.dump(data, f, indent=4)






    



