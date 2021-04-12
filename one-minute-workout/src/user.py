class User:
    def __init__(self, username:str):
        self.username = username
    
    def setPassword(self, password:str):
        self.password = password

    def __str__(self):
        return f"username: {self.username}"
    