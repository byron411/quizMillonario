#Clase que representa las respuestas
class Respuesta:
    def __init__(self,pId:int,pDescripcion:str):
        '''Método constructor de la clase Respuesta'''
        self.__id=pId
        self.__descripcion=pDescripcion
    #Métodos getters
    def darId(self):
        return self.__id
    def darDescripcion(self):
        return self.__descripcion

