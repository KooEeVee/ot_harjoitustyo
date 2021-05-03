import json


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # add new user to users.json file:

    def new_user_json(self):
        user = {
            "username": self.username,
            "password": self.password,
            "timer_start": "00:00",
            "timer_stop": "00:00",
            "timer_interval": "00"
        }
        with open("src/users.json", "r") as f:
            data = json.load(f)
            data["users"].append(user)

        with open("src/users.json", "w") as f:
            json.dump(data, f, indent=4)

    def get_user_json(self):
        with open("src/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user.get("username") == self.username:
                    return True

    def get_password_json(self, username):
        with open("src/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user.get("username") == username:
                    return user.get("password")

    def get_timer_json(self):
        with open("src/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user["username"] == self.username:
                    start = user.get("timer_start")
                    stop = user.get("timer_stop")
                    interval = user.get("timer_interval")
                    return f"Start time: {start}, End time: {stop}, Interval: {interval}"

    def get_timer_start(self):
        with open("src/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user["username"] == self.username:
                    start = user.get("timer_start")
                    return start

    def get_timer_stop(self):
        with open("src/users.json", "r") as f:
            data = json.load(f)
            for user in data["users"]:
                if user["username"] == self.username:
                    stop = user.get("timer_stop")
                    return stop

    def get_timer_interval(self):
        with open("src/users.json", "r") as f:
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
