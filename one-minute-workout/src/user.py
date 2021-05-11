import json


class User:
    """Class to save and update user data.

    Attributes:
        username (String): username that user sets in signup process
        password (String): password thatuser sets in login process
    """
    def __init__(self, username, password):
        """Class constructor to create new user.

        Args:
            username (String): username that user sets in signup process
            password (String): password thatuser sets in login process
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
        with open("src/db/users.json", "r") as f:
            data = json.load(f)
            data["users"].append(user)

        with open("src/db/users.json", "w") as f:
            json.dump(data, f, indent=4)

    def get_user_json(self):
        """Check if username already exists in users.json file.

        Returns:
            (Boolean): True if username already exists
        """
        with open("src/db/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user.get("username") == self.username:
                    return True

    def get_password_json(self, username):
        """Get user's password.

        Args:
            username (String): username saved in users.json file

        Returns:
            (String): password saved with the username in users.json file
        """
        with open("src/db/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user.get("username") == username:
                    return user.get("password")

    def get_timer_json(self):
        """Get user's timer end time and interval.

        Returns:
            (String): timer end time and interval saved with the username in users.json file
        """
        with open("src/db/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user["username"] == self.username:
                    stop = user.get("timer_stop")
                    interval = user.get("timer_interval")
                    return f"End time: {stop}. Interval: {interval} minutes."

    def get_timer_stop(self):
        """Get user's timer end time.

        Returns:
            (String): timer end time saved with the username in users.json file
        """
        with open("src/db/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user["username"] == self.username:
                    stop = user.get("timer_stop")
                    return stop

    def get_timer_interval(self):
        """Get user's timer interval.

        Returns:
            (String): timer interval saved with the username in users.json file
        """
        with open("src/db/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user["username"] == self.username:
                    interval = user.get("timer_interval")
                    return interval

    # add new user to users.csv file
    # def new_user_csv(self):
    #     with open("src/users.csv", "a") as f:
    #         w = csv.writer(f, delimiter=',')
    #         w.writerow([self.username, self.password])

    # def get_username_csv(self, username):
    #     with open("src/users.csv", newline="") as f:
    #         r = csv.reader(f, delimiter=',')
    #         for row in r:
    #             if row[0] == username:
    #                 return True

    # def get_password_csv(self, username):
    #     with open("src/users.csv", newline="") as f:
    #         r = csv.reader(f, delimiter=',')
    #         for row in r:
    #             if row[0] == username:
    #                 return row[1]

    # add new user to users table AWS RDS PostgreSQL
    # def new_user_db(self):
    #     db = Database(DATABASE_ENDPOINT, DATABASE_USERNAME,
    #                   DATABASE_PASSWORD, DATABASE_NAME)
    #     db.connect_db()
    #     db.insert_user(self.username, self.password)
    #     db.disconnect_db()

    # def get_username_db(self, username):
    #     db = Database(DATABASE_ENDPOINT, DATABASE_USERNAME,
    #                   DATABASE_PASSWORD, DATABASE_NAME)
    #     db.connect_db()
    #     self.username = db.select_username(username)
    #     db.disconnect_db()

    # def get_password_db(self, username):
    #     db = Database(DATABASE_ENDPOINT, DATABASE_USERNAME,
    #                   DATABASE_PASSWORD, DATABASE_NAME)
    #     db.connect_db()
    #     self.password = db.select_password(username)
    #     db.disconnect_db()

    def __str__(self):
        return f"username: {self.username}"
