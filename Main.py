import os
import sys

# Agregamos el directorio padre al path de python
PROJECT_ROOT = os.path.abspath(
                os.path.join(
                os.path.dirname(__file__), 
                os.pardir))
sys.path.append(PROJECT_ROOT)
# os.path.dirname(__file__) devuelve el directorio del archivo actual
# os.pardir devuelve el nombre del directorio padre
# os.path.join une los dos directorios
# os.path.abspath devuelve la ruta absoluta del directorio
# sys.path.append agrega el directorio al path de python

from View.MainMenu import MainMenu

if __name__ == "__main__":
    MainMenu.Menu()
