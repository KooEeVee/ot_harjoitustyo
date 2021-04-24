import json

class Timer:
    def __init__(self, start, stop, interval, user):
        self.timer_start = start
        self.timer_stop = stop
        self.interval = interval
        self.user = user

    def save_timer_to_user(self):
        with open ("src/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user["username"] == self.user:
                    user["timer_start"] = self.timer_start
                    user["timer_stop"] = self.timer_stop
                    user["timer_interval"] = self.interval
    
        with open ("src/users.json", "w") as f:
            json.dump(data, f, indent=4)






    



