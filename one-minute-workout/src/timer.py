import json


class Timer:
    def __init__(self, stop, interval, username):
        """Class to save and update timer data.

        Attributes:
            start (String): timer start time HH:MM
            stop (String): timer stop time HH:MM
            interval (String): timer interval
            username (String): username saved in the users.json file

        """
        # self.timer_start = start
        self.timer_stop = stop
        self.interval = interval
        self.username = username
        """Class constructor to create new timer.

        Args:
            start (String): timer start time HH:MM
            stop (String): timer stop time HH:MM
            interval (String): timer interval
            username (String): username saved in the users.json file
        """

    def save_timer_to_user(self):
        """Save timer data to user data in users.json file.

        """
        with open("src/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user["username"] == self.username:
                    # user["timer_start"] = self.timer_start
                    user["timer_stop"] = self.timer_stop
                    user["timer_interval"] = self.interval

        with open("src/users.json", "w") as f:
            json.dump(data, f, indent=4)

    def get_timer_from_user(self):
        """Get timer data from user saved in users.json file.

        Returns:
            [String]: Start time: 00:00, End time: 00:00, Interval: 00"
        """
        with open("src/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user["username"] == self.username:
                    # start = user.get("timer_start")
                    end = user.get("timer_stop")
                    interval = user.get("timer_interval")
                    return f"End time: {end}, Interval: {interval}"

    def __str__(self):
        return f"End time: {self.timer_stop}, exercise interval: {self.interval}"
