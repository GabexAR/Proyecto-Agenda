class UserForCreation:
    username = ""
    password = ""
    email = ""
    surname = ""

    def __init__(self, username, password, email, name, surname):
        self.username = username
        self.email = email
        self.name = name
        self.surname = surname
        self.password = password