from os import system
import sys

from .ContactView import ContactView
from .UserView import UserView

class MainMenu:
    @classmethod
    def Menu(cls):
        while True:
            system("cls")
            print(" Bienvenido a la agenda de contactos ".center(50, "#"))
            print("1. Login de usuario")
            print("2. Registro de usuario")
            print("3. Listar Usuarios")
            print("4. Salir del programa")
            print("-" * 50)
            option = input("Ingrese una opcion: ")
            if option == "1":
                validation = UserView.loginMenu()
                if validation[0] == True:
                    user = validation[1]
                    ContactView(user).Menu()
                else:
                    print(" Usuario o contraseña incorrecta ".center(50, "!"))
                    input(" Presione enter para continuar ".center(50, "!"))
            elif option == "2":
                UserView.addUserMenu()
            elif option == "3":
                UserView.listUsers()
            elif option == "4":
                break
            else:
                print(" Opcion incorrecta ".center(50, "!"))
                input(" Presione enter para continuar ".center(50, "!"))


if __name__ == "__main__":
    MainMenu.Menu()