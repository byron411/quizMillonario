#Clase principal del juego quizMillonario
from clases.mundo.Jugador import *
from clases.mundo.Pregunta import *
from clases.mundo.Respuesta import *
import sqlite3
class Millonario:
    def __init__(self):
        '''Método constructor de la clase Millonario'''
        self.__jugadores=[]
        self.cargarJugadores()
        '''cargar preguntas'''
        self.__preguntas = []
        self.cargarPreguntas()
        '''cargar respuestas'''
        self.__respuestas=[]
        self.cargarRespuestas()

    #Métodos getters
    def darJugadores(self):
        return self.__jugadores
    def darPreguntas(self):
        return self.__preguntas
    def darRespuestas(self):
        return self.__respuestas
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
        try:
            miConexion=sqlite3.connect('../../data/bd/millonario.db')
            miCursor=miConexion.cursor()
            miCursor.execute('select * from pregunta')
            recibidas=miCursor.fetchall()
            #print(len(recibidas))
            miConexion.close()
            for i in range(len(recibidas)):
                pregunta=Pregunta(recibidas[i][0],recibidas[i][1],recibidas[i][2],recibidas[i][3])
                self.__preguntas.append(pregunta)
        except Exception as e:
            pass
    def cargarRespuestas(self):
        miConexion=sqlite3.connect('../../data/bd/millonario.db')
        miCursor=miConexion.cursor()
        miCursor.execute('select * from respuesta')
        resRecibidas=miCursor.fetchall()
        miConexion.close()
        for i in range(len(resRecibidas)):
            respuesta=Respuesta(resRecibidas[i][0],resRecibidas[i][1],resRecibidas[i][2])
            self.__respuestas.append(respuesta)

    def buscarRespuestaPorId(self,pId):
        encontrado=False
        respuesta=None
        i=0
        while i< len(self.__respuestas) and not encontrado:
            if self.__respuestas[i].darId()==pId:
                encontrado=True
                respuesta=self.__respuestas[i]
            i+=1
        return respuesta
    def buscarRespuestaPorTipo(self,pTipo):
        respuestasPorTipo=[]
        for i in range(len(self.__respuestas)):
            tipo=self.__respuestas[i].darTipo()
            if tipo==pTipo:
                respuestasPorTipo.append(self.__respuestas[i])
        return respuestasPorTipo
    def buscarRespuestaPorDescripcion(self,pDescripcion):
        encontrado=False
        i=0
        respuesta=None
        while i< len(self.__respuestas) and not encontrado:
            if self.__respuestas[i].darDescripcion()==pDescripcion:
                encontrado=True
                respuesta=self.__respuestas[i]
            i+=1
        return respuesta
    def buscarPreguntaPorIdRespuesta(self,pIdRespuesta):
        encontrado = False
        i = 0
        pregunta = None
        while i < len(self.__preguntas) and not encontrado:
            if self.__preguntas[i].darIdRespuesta() == pIdRespuesta:
                encontrado = True
                pregunta = self.__preguntas[i]
            i += 1
        return pregunta
    def actualizarYouLost(self, pJugador):
        pJugador.setJugados(pJugador.darJugados()+1)
        pJugador.setPerdidos(pJugador.darPerdidos()+1)
        miConexion=sqlite3.connect('../../data/bd/millonario.db')
        miCursor=miConexion.cursor()
        miCursor.execute('update jugador set jugados=?,perdidos=? where id=?',(pJugador.darJugados(),pJugador.darPerdidos(),pJugador.darId()))
        miConexion.commit()
        miConexion.close()

    def actualizarYouWin(self, pJugador, pAcumulado):
        pJugador.setJugados(pJugador.darJugados()+1)
        pJugador.setGanados(pJugador.darGanados() + 1)
        total=pAcumulado+pJugador.darAcumulado()
        pJugador.setAcumulado(total)
        miConexion=sqlite3.connect('../../data/bd/millonario.db')
        miCursor=miConexion.cursor()
        miCursor.execute('update jugador set acumulado=?,jugados=?,ganados=? where id=?',(total,pJugador.darJugados(),pJugador.darGanados(),pJugador.darId()))
        miConexion.commit()
        miConexion.close()
    def buscarJugadorPorNombre(self,pNombre):
        i=0
        encontrado=False
        jugador=None
        while i< len(self.__jugadores) and not encontrado:
            if self.__jugadores[i].darNombre()==pNombre:
                encontrado=True
                jugador=self.__jugadores[i]
            i+=1
        return jugador


#princial=Millonario()
#princial.cargarJugadores()
#princial.cargarPreguntas()
#princial.cargarRespuestas()