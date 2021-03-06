import json


class User:
    """Class to save and update user data.

    Save username, password, timer stop 00:00 and timer interval 00.

    Attributes:
        username: username string that user sets in signup process
        password: password string that user sets in signup process
    """

    def __init__(self, username, password):
        """Class constructor to create new user.

        Args:
            username: username string that user sets in signup process
            password: password string that user sets in signup process
        """
        self.username = username
        self.password = password

    def new_user_json(self):
        """Save new user in users.json file."""
        user = {
            "username": self.username,
            "password": self.password,
            "timer_stop": "00:00",
            "timer_interval": "00"
        }
        with open("src/db/users.json", "r") as file:
            data = json.load(file)
            data["users"].append(user)

        with open("src/db/users.json", "w") as file:
            json.dump(data, file, indent=4)

    def get_user_json(self):
        """Check if username already exists in users.json file.

        Returns:
            True if username exists
        """
        with open("src/db/users.json", "r") as file:
            data = json.load(file)
            for user in data["users"]:
                if user.get("username") == self.username:
                    return True

    def get_password_json(self, username):
        """Get user's password.

        Args:
            username: username saved in users.json file

        Returns:
            Password saved with the username in users.json file
        """
        with open("src/db/users.json", "r") as file:
            data = json.load(file)
            for user in data["users"]:
                if user.get("username") == username:
                    return user.get("password")

    def get_timer_json(self):
        """Get user's timer end time and interval.

        Returns:
            Timer end time and interval string saved with the username in users.json file
        """
        with open("src/db/users.json", "r") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == self.username:
                    stop = user.get("timer_stop")
                    interval = user.get("timer_interval")
                    return f"End time: {stop}. Interval: {interval} minutes."

    def get_timer_stop(self):
        """Get user's timer end time.

        Returns:
            Timer end time string saved with the username in users.json file
        """
        with open("src/db/users.json", "r") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == self.username:
                    stop = user.get("timer_stop")
                    return stop

    def get_timer_interval(self):
        """Get user's timer interval.

        Returns:
            Timer interval string saved with the username in users.json file
        """
        with open("src/db/users.json", "r") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == self.username:
                    interval = user.get("timer_interval")
                    return interval

    def __str__(self):
        return f"username: {self.username}"
