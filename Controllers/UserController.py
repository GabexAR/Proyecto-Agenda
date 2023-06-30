from Model.DTO.UserForLogin import UserForLogin
from Model.Repository.UserRepository import UserRepository
from Model.DTO.UserForView import UserForView

class UserController:
    def get_users(self):
        user_repository = UserRepository()
        users = user_repository.get_users()
        usersForView = []
        for user in users:
            userForView = UserForView(user)
            usersForView.append(userForView)
        return usersForView
    
    def get_user(self, user):
        user_repository = UserRepository()
        userRP = user_repository.get_user(user)
        if userRP == None:
            return None
        else:
            userForView = UserForView(userRP)
            return userForView
    
    def add_user(self, user):
        user_repository = UserRepository()
        user_repository.add_user(user)

        
    def update_user(self, user):
        user_repository = UserRepository()
        user_repository.update_user(user)

    def delete_user(self, user):
        user_repository = UserRepository()
        user_repository.delete_user(user)

    def login(self, user):
        user_repository = UserRepository()
        userRP = user_repository.get_user(user)
        if userRP == None:
            return False, None
        else:
            userValidated = UserForLogin(userRP.username, userRP.password)
            if userRP.password == user.password:
                return True, userValidated
            else:
                return False, userValidated
    