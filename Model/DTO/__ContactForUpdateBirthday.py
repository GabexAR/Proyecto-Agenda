class ContactForUpdateBirthday:
    id = 0
    name = ""
    surname = ""
    email = "" 
    birthday = ""
    username = ""    
    state = 1

    def __init__(self, id, name, surname, email, birthday, username) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.birthday = birthday
        self.username = username
        self.state = 1
