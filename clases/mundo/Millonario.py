#Clase principal del juego quizMillonario
from clases.mundo.Jugador import *
from clases.mundo.Pregunta import *
import sqlite3
class Millonario:
    def __init__(self):
        '''Método constructor de la clase Millonario'''
        self.__jugadores=[]
        self.cargarJugadores()
        '''cargar preguntas'''
        self.__preguntas = []
        self.cargarPreguntas()

    #Métodos getters
    def darJugadores(self):
        return self.__jugadores
    def darPreguntas(self):
        return self.__preguntas
    #Métodos
    def cargarJugadores(self):
        '''()->void Carga los jugadores existentes en la base de datos y los carga en un array
        @:except Lanza una excepción si no encuentra la base de datos'''
        try:
            conexion=sqlite3.connect('../../data/bd/millonario.db')
            miCursor=conexion.cursor()
            miCursor.execute('select * from jugador order by nombre asc')
            recibidos=miCursor.fetchall()
            conexion.close()
            for i in range(len(recibidos)):
                jugador=Jugador(recibidos[i][0],recibidos[i][1],recibidos[i][2],recibidos[i][3],recibidos[i][4],
                                recibidos[i][5],recibidos[i][6])
                self.__jugadores.append(jugador)
        except Exception as e:
            #raise Exception('Hubo un error '+str(e))
            print('Hubo un error: '+str(e))


    def agregarJugador(self,pNombre):
        '''()-> Void Agrega un jugador a la base de datos y a un array
        @:parameter pNombre nombre del jugador
        @:except Lanza una excepción si no encuentra la base de datos
        @:except Lanza una excepción si se duplica el nombre:UNIQUE'''
        try:
            conexion=sqlite3.connect('../../data/bd/millonario.db')
            miCursor=conexion.cursor()
            jugador=[(pNombre,0,0,0,0,0)]
            miCursor.executemany('insert into jugador values(null,?,?,?,?,?,?)',jugador)
            miCursor.execute('select id from jugador where nombre=?',(pNombre,))
            recibido=miCursor.fetchone()
            pId=recibido[0]
            conexion.commit()
            conexion.close()
            self.__jugadores.append(Jugador(pId,pNombre,0,0,0,0,0))
        except Exception as e:
            raise Exception('Ha ocurrido un error: '+str(e))
    def cargarPreguntas(self):
        miConexion=sqlite3.connect('../../data/bd/millonario.db')
        miCursor=miConexion.cursor()
        miCursor.execute('select * from pregunta')
        recibidas=miCursor.fetchall()
        #print(len(recibidas))
        miConexion.close()
        for i in range(len(recibidas)):
            pregunta=Pregunta(recibidas[i][0],recibidas[i][1],recibidas[i][2],recibidas[i][3])
            self.__preguntas.append(pregunta)

#princial=Millonario()
#princial.cargarJugadores()
#princial.cargarPreguntas()