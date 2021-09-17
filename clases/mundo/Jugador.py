#clase que representa a un jugador del juego
class Jugador:
    def __init__(self, pId:int, pNombre:str, pAcumulado:float, pJugados:int, pRetirados:int,pGanados:int):
        '''Método constructor de la clase Jugador'''
        self.__id=pId
        self.__nombre=pNombre
        self.__acumulado=pAcumulado
        self.__jugados=pJugados
        self.__retirados=pRetirados
        self.__ganados=pGanados
    #Métodos getter
    def darId(self):
        return self.__id
    def darNombre(self):
        return self.__nombre
    def darAcumulado(self):
        return self.__acumulado
    def darJugados(self):
        return self.__jugados
    def darRetirados(self):
        return self.__retirados
    def darGanados(self):
        return self.__ganados
    #Métodos normales