from application import Application


def main():

    app = Application()
    app.initialize_users_json()
    app.initialize_ui()


if __name__ == "__main__":
    main()
