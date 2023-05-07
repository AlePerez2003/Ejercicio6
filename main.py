from manejador_viajero import Lista_viajero
from viajero import Viajero_frecuente
from menu import Menu

if __name__ == '__main__':
    opciones = Menu()
    listaViajeros = Lista_viajero()
    listaViajeros.test_lista_viajero()
    listaViajeros.mostrar_viajeros()
    opciones.menu(listaViajeros)