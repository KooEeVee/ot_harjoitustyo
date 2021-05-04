import psycopg2


class Database:
    def __init__(self, DATABASE_ENDPOINT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME):
        self.endpoint = DATABASE_ENDPOINT
        self.username = DATABASE_USERNAME
        self.password = DATABASE_PASSWORD
        self.name = DATABASE_NAME
        self.conn = None
        self.cur = None

    def connect_db(self):
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.endpoint, user=self.username, password=self.password, dbname=self.name)
                self.cur = self.conn.cursor()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    def insert_user(self, user_username, user_password):
        user = (user_username, user_password)
        query = ("INSERT INTO users (username, password) VALUES (%s, %s)")

        if self.conn is not None:
            try:
                self.cur.execute(query, user)
                self.conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    def select_username(self, user_username):
        user = (user_username,)
        query = ("SELECT username FROM users WHERE username = (%s)")

        if self.conn is not None:
            try:
                self.cur.execute(query, user)
                self.conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        return self.cur.fetchone()

    def select_password(self, user_username):
        user = (user_username,)
        query = ("SELECT password FROM users WHERE username = (%s)")

        if self.conn is not None:
            try:
                self.cur.execute(query, user)
                self.conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        return self.cur.fetchone()

    def get_rows(self):
        query = ("SELECT COUNT(*) FROM users")

        if self.conn is not None:
            try:
                self.cur.execute(query)
                self.conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        return self.cur

    def disconnect_db(self):
        if self.conn is not None:
            self.cur.close()
            self.conn.close()
