class ContactForUpdate:
    id = 0
    name = ""
    surname = ""
    email = ""
    username = ""
    state = 1
    birthday = ""

    def __init__(self, id, name, surname, email, username) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.username = username
        self.state = 1
        self.birthday = None
