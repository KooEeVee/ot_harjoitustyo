import csv
from user import User

def main():
    user = User("KooEeVee", "1234")
    user.newUser()

    with open("src/users.csv", "r") as f:
        r = csv.reader(f, delimiter=',')
        for row in r:
            print(row)

if __name__ == "__main__":
    main()

