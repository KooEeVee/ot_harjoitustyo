import json

class Application:
    def __init__(self):
        self.test = None

    def initialize_json(self):
        data = {}
        data["users"] = []
        with open ("src/users.json", "a") as f:
            json.dump(data, f, indent=4)
