class User():
    username = ""
    password = ""
    email = ""
    name = ""
    surname = ""
    state = True

    def __repr__(self) -> str:
        return f"User(username={self.username}, password={self.password}, email={self.email}, name={self.name}, surname={self.surname}, state={self.state})"

    
