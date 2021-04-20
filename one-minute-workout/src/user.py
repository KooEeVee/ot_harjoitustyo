from database import Database
import csv
from config import DATABASE_ENDPOINT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # add new user to users.csv file
    def new_user_csv(self):
        with open("src/users.csv", "a") as f:
            w = csv.writer(f, delimiter=',')
            w.writerow([self.username, self.password])

    def get_username_csv(self, username):
        with open("src/users.csv", newline="") as f:
            r = csv.reader(f, delimiter=',')
            for row in r:
                if row[0] == username:
                    return True

    def get_password_csv(self, username):
        with open("src/users.csv", newline="") as f:
            r = csv.reader(f, delimiter=',')
            for row in r:
                if row[0] == username:
                    return row[1]

    # add new user to users table AWS RDS PostgreSQL
    def new_user_db(self):
        db = Database(DATABASE_ENDPOINT, DATABASE_USERNAME,
                      DATABASE_PASSWORD, DATABASE_NAME)
        db.connect_db()
        db.insert_user(self.username, self.password)
        db.disconnect_db()

    def get_username_db(self, username):
        db = Database(DATABASE_ENDPOINT, DATABASE_USERNAME,
                      DATABASE_PASSWORD, DATABASE_NAME)
        db.connect_db()
        self.username = db.select_username(username)
        db.disconnect_db()

    def get_password_db(self, username):
        db = Database(DATABASE_ENDPOINT, DATABASE_USERNAME,
                      DATABASE_PASSWORD, DATABASE_NAME)
        db.connect_db()
        self.password = db.select_password(username)
        db.disconnect_db()

    def __str__(self):
        return f"username: {self.username}"
