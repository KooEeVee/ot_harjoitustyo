import json


class Timer:
    """Class to save and update timer data.

    Save timer stop and timer interval with the user data.

    Attributes:
        stop: timer stop time string HH:MM
        interval: timer interval string MM
        username: username string saved in the users.json file
    """

    def __init__(self, stop, interval, username):
        """Class constructor to create a timer.

        Args:
            stop: timer stop time string HH:MM
            interval: timer interval string MM
            username: username string saved in the users.json file
        """
        self.timer_stop = stop
        self.interval = interval
        self.username = username

    def save_timer_to_user(self):
        """Save timer data to user data in users.json file."""
        with open("src/db/users.json", "r") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == self.username:
                    user["timer_stop"] = self.timer_stop
                    user["timer_interval"] = self.interval

        with open("src/db/users.json", "w") as file:
            json.dump(data, file, indent=4)

    def get_timer_from_user(self):
        """Get timer data from user saved in users.json file.

        Returns:
            String End time: 00:00, Interval: 00"
        """
        with open("src/db/users.json", "r") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == self.username:
                    end = user.get("timer_stop")
                    interval = user.get("timer_interval")
                    return f"End time: {end}, Interval: {interval}"

    def __str__(self):
        return f"End time: {self.timer_stop}, exercise interval: {self.interval}"
