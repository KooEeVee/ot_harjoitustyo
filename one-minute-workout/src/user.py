from database import Database
from config import DATABASE_ENDPOINT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # add new user to users.csv file
    #def new_user(self):
        #with open("src/users.csv", "a") as f:
            #w = csv.writer(f, delimiter=',')
            #w.writerow([self.username, self.password])

    # add new user to users table AWS RDS PostgreSQL
    def new_user_db(self):
        db = Database(DATABASE_ENDPOINT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME)
        db.connect_db()
        db.insert_user(self.username, self.password)
        db.disconnect_db
        
    def __str__(self):
        return f"username: {self.username}"
