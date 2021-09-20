#Clase que representa las respuestas
class Respuesta:
    def __init__(self,pId:int,pDescripcion:str,pTipo:str):
        '''Método constructor de la clase Respuesta'''
        self.__id=pId
        self.__descripcion=pDescripcion
        self.__tipo=pTipo
    #Métodos getters
    def darId(self):
        return self.__id
    def darDescripcion(self):
        return self.__descripcion
    def darTipo(self):
        return self.__tipo
    #Método str
    def __str__(self):
        return self.__descripcion

