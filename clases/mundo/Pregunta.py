#Clase que representa una pregunta del juego
from clases.mundo.Categoria import *
class Pregunta:
    def __init__(self, pId:int, pDescripcion:str, pCategoria:Categoria):
        '''Método constructor de la clase Pregunta'''
        self.__id=pId
        self.__descripcion=pDescripcion
        self.__categoria=pCategoria

    #Métodos getters
    def darId(self):
        return self.__id
    def darDescripcion(self):
        return self.__descripcion
    def darCategoria(self):
        return self.__categoria
    #Métodos normales