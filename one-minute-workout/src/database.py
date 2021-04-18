import psycopg2

class Database:
    def __init__(self, DATABASE_ENDPOINT, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME):
        self.endpoint = DATABASE_ENDPOINT
        self.username = DATABASE_USERNAME
        self.password = DATABASE_PASSWORD
        self.name = DATABASE_NAME
        self.conn = None

    def insert_user(self, user_username, user_password):
        user = (user_username, user_password)
        query = ("INSERT INTO users (username, password) VALUES (%s, %s)")

        if self.conn is None:

            try:
                self.conn = psycopg2.connect(host=self.endpoint, user=self.username, password=self.password, dbname=self.name)
                cur = self.conn.cursor()
                cur.execute(query, user)
                self.conn.commit()
                cur.close()

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if self.conn is not None:
                    self.conn.close()

