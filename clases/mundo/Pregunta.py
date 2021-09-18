#Clase que representa una pregunta del juego
from clases.mundo.Categoria import *
class Pregunta:
    def __init__(self, pId:int, pDescripcion:str, pCategoria:Categoria,pIdRespuesta:int):
        '''Método constructor de la clase Pregunta'''
        self.__id=pId
        self.__descripcion=pDescripcion
        self.__categoria=pCategoria
        self.__idRespuesta=pIdRespuesta

    #Métodos getters
    def darId(self):
        return self.__id
    def darDescripcion(self):
        return self.__descripcion
    def darCategoria(self):
        return self.__categoria
    def darIdRespuesta(self):
        return self.__idRespuesta
    #Métodos normales

    #Método str
    def __str__(self):
        return self.__descripcion