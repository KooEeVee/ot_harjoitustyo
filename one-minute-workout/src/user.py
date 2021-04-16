import csv


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # add new user to users.csv file
    def new_user(self):
        with open("src/users.csv", "a") as f:
            w = csv.writer(f, delimiter=',')
            w.writerow([self.username, self.password])

    def __str__(self):
        return f"username: {self.username}"
