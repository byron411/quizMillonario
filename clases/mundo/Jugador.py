#clase que representa a un jugador del juego
class Jugador:
    def __init__(self, pId:int, pNombre:str, pAcumulado:float, pJugados:int,pGanados:int,pPerdidos:int,pRetirados):
        '''Método constructor de la clase Jugador'''
        self.__id=pId
        self.__nombre=pNombre
        self.__acumulado=pAcumulado
        self.__jugados=pJugados
        self.__ganados = pGanados
        self.__perdidos=pPerdidos
        self.__retirados=pRetirados

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
    def darPerdidos(self):
        return self.__perdidos;
    #Métodos normales

    def __str__(self):
        '''()->str devuelve el formato de un objeto Jugador
        @:return nombre'''
        return self.__nombre