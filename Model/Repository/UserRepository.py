
from ..Entities.User import User
from ..Context import Context

class UserRepository:

    def get_users(self):
        with Context() as context1:
            query = "SELECT * FROM user WHERE state = 1"
            context1.mycursor.execute(query)
            usersDB = context1.mycursor.fetchall()

        users = []
        for userDB in usersDB:
            user = User()
            user.username = userDB[0]
            user.password = userDB[1]
            user.email = userDB[2]
            user.name = userDB[3]
            user.surname = userDB[4]
            user.state = userDB[5]
            users.append(user)
        return users
    
    def get_user(self, user):
        with Context() as context1:
            query = "SELECT * FROM user WHERE username = %s"
            values = (user.username,)
            context1.mycursor.execute(query, values)
            userDB = context1.mycursor.fetchone()
        if userDB:
            user = User()
            user.username = userDB[0]
            user.password = userDB[1]
            user.email = userDB[2]
            user.name = userDB[3]
            user.surname = userDB[4]
            user.state = userDB[5]
            return user
        return None

    def add_user(self, user):
        with Context() as context1:
            query = "INSERT INTO user (username, password, email, name, surname, state) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (user.username, user.password, user.email, user.name, user.surname, 1)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
            

    def update_user(self, user):
        with Context() as context1:
            query = "UPDATE user SET username = %s, password = %s, email = %s, name = %s, surname = %s WHERE username = %s"
            values = (user.username, user.password, user.email, user.name, user.surname, user.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()

    def delete_user(self, user):
        with Context() as context1:
            query = "UPDATE user SET state = %s WHERE username = %s"
            values = (0, user.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
