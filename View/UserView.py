
from os import system
from Controllers.UserController import UserController
from Model.DTO.UserForCreation import UserForCreation
from Model.DTO.UserForLogin import UserForLogin


class UserView:

    @classmethod
    def addUserMenu(cls):
        system("cls")
        print(" Alta de usuario ".center(50, "#"))
        print("-"*50)
        username = input("Ingrese el nombre de usuario: ")
        print("-"*50)
        password = input("Ingrese la contraseña: ")
        print("-"*50)
        email = input("Ingrese el email: ")
        print("-"*50)
        name = input("Ingrese el nombre: ")
        print("-"*50)
        surname = input("Ingrese el apellido: ")
        print("-"*50)
        userFC = UserForCreation(username, password, email, name, surname)
        userController1 = UserController()
        userController1.add_user(userFC)
        input(" Presione enter para continuar ".center(50, "!"))
        return
    
    @classmethod
    def loginMenu(cls):
        system("cls")
        print(" Login de usuario ".center(50, "#"))
        print("-"*50)
        username = input("Ingrese el nombre de usuario: ")
        print("-"*50)
        password = input("Ingrese la contraseña: ")
        print("-"*50)
        input(" Presione enter para continuar ".center(50, "!"))
        userController1 = UserController()
        userForLogin1 = UserForLogin(username, password)
        validation = userController1.login(userForLogin1)
        return validation
    
    @classmethod
    def listUsers(cls):
        system("cls")
        print(" Listado de usuarios ".center(50, "#"))
        userC = UserController()
        users = userC.get_users()
        for user in users:
            print(user)
        print("#"*50)
        input(" Presione enter para continuar ".center(50, "!"))

