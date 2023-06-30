class UserForView:
    username = ""
    password = ""
    email = ""
    surname = ""

    def __init__(self, user):
        self.username = user.username
        self.email = user.email
        self.name = user.name
        self.surname = user.surname

    def __str__(self) -> str:
        return f"Username: {self.username} - Email: {self.email} - Name: {self.name} - Surname: {self.surname}"