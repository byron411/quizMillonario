#Clase principal del juego quizMillonario
from clases.mundo.Jugador import *
from clases.mundo.Pregunta import *
from clases.mundo.Respuesta import *
import sqlite3
class Millonario:
    def __init__(self):
        '''Método constructor de la clase Millonario'''
        #Array jugadores
        self.__jugadores=[]
        self.cargarJugadores()
        '''cargar preguntas'''
        # Array preguntas
        self.__preguntas = []
        self.cargarPreguntas()
        '''cargar respuestas'''
        #Array respuestas
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
        '''()->void. Carga las preguntas de la base de datos
        @:exception lanza una excepción si no encuentra la base de datos'''
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
            print('Error cargando preguntas '+str(e))
    def cargarRespuestas(self):
        '''()->void. Carga las respuestas de la base de datos y las agrega a un array
        @:exception lanza una excepción si no puede cargar las respuestas'''
        try:
            miConexion=sqlite3.connect('../../data/bd/millonario.db')
            miCursor=miConexion.cursor()
            miCursor.execute('select * from respuesta')
            resRecibidas=miCursor.fetchall()
            miConexion.close()
            for i in range(len(resRecibidas)):
                respuesta=Respuesta(resRecibidas[i][0],resRecibidas[i][1],resRecibidas[i][2])
                self.__respuestas.append(respuesta)
        except Exception as e:
            print('error cargando respuestas'+str(e))

    def buscarRespuestaPorId(self,pId):
        '''()->Respuesta Busca una respuesta dado el id
                @:parameter pId id de respuesta a buscar
                @:return Respuesta devuelve una Respuesta, None en caso contrario'''
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
        '''()->Respuesta Busca una respuesta dado el ipo
        @:parameter pTipo tipo de respuesta a buscar
        @:return Respuesta devuelve una Respuesta, None en caso contrario'''
        respuestasPorTipo=[]
        for i in range(len(self.__respuestas)):
            tipo=self.__respuestas[i].darTipo()
            if tipo==pTipo:
                respuestasPorTipo.append(self.__respuestas[i])
        return respuestasPorTipo
    def buscarRespuestaPorDescripcion(self,pDescripcion):
        '''()->Respuesta Busca una respuesta dada la descripción
            @:parameter pDescripcion descripcion de respuesta a buscar
            @:return Respuesta devuelve una Respuesta, None en caso contrario'''
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
        '''()->Pregunta Busca una pregunta dado el id de respuesta
        @:parameter pIdRespuesta id de respuesta
        @:return Pregunta devuelve una Respuesta, None en caso contrario'''
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
        '''()-void. actualiza jugados y perdidos de un jugador
        @:parameter pJugador Jugador al que se le debe actualizar los perdidos'''

        pJugador.setJugados(pJugador.darJugados()+1)
        pJugador.setPerdidos(pJugador.darPerdidos()+1)
        try:
            miConexion=sqlite3.connect('../../data/bd/millonario.db')
            miCursor=miConexion.cursor()
            miCursor.execute('update jugador set jugados=?,perdidos=? where id=?',(pJugador.darJugados(),pJugador.darPerdidos(),pJugador.darId()))
            miConexion.commit()
            miConexion.close()
        except Exception as e:
            print('error actualizando yourlost'+str(e))

    def actualizarYouWin(self, pJugador, pAcumulado):
        '''()-void. actualiza jugados, ganados y acumulado de un jugador
        @:parameter pJugador Jugador al que se le debe actualizar los juegos ganados
        @:parameter pAcumulado el acumulado mayor'''
        try:
            pJugador.setJugados(pJugador.darJugados()+1)
            pJugador.setGanados(pJugador.darGanados() + 1)
            total=pAcumulado+pJugador.darAcumulado()
            pJugador.setAcumulado(total)
            miConexion=sqlite3.connect('../../data/bd/millonario.db')
            miCursor=miConexion.cursor()
            miCursor.execute('update jugador set acumulado=?,jugados=?,ganados=? where id=?',(total,pJugador.darJugados(),pJugador.darGanados(),pJugador.darId()))
            miConexion.commit()
            miConexion.close()
        except Exception as e:
            print('Error actualizando ganados youWin '+str(e))
    def actualizarYouDraw(self,pJugador,pAcumulado):
        '''()-void. actualiza jugados, retirados de un jugador
        @:parameter pJugador Jugador al que se le debe actualizar los juegos retirados
        @:parameter pAcumulado el acumulado actual'''
        try:
            pJugador.setJugados(pJugador.darJugados() + 1)
            total = pAcumulado + pJugador.darAcumulado()
            pJugador.setAcumulado(total)
            pJugador.setRetirados(pJugador.darRetirados()+1)
            miConexion=sqlite3.connect('../../data/bd/millonario.db')
            miCursor=miConexion.cursor()
            miCursor.execute('update jugador set acumulado=?, jugados=?,retirados=? where id=?',(total,pJugador.darJugados(),pJugador.darRetirados(),pJugador.darId()))
            miConexion.commit()
            miConexion.close()
        except Exception as e:
            print('Error actualizando los retirados')
    def buscarJugadorPorNombre(self,pNombre):
        '''()->Jugador Busca un jugador dado el nombre
        @:parameter pNombre nombre a buscar
        @:return Respuesta devuelve un Jugador, None en caso contrario'''
        i=0
        encontrado=False
        jugador=None
        while i< len(self.__jugadores) and not encontrado:
            if self.__jugadores[i].darNombre()==pNombre:
                encontrado=True
                jugador=self.__jugadores[i]
            i+=1
        return jugador
    def actualizarJugador(self,pNombre, pId):
        '''()-> void. Actualiza un jugador dado el id de jugador
        @:parameter: pNombre nuevo nombre de jugador
        @:parameter: pId id del jugador a actualizar nombre
        @:except: Lanza una excepción si no logra actualizar'''
        #try:
        miConexion = sqlite3.connect('../../data/bd/millonario.db')
        miCursor = miConexion.cursor()
        miCursor.execute('update jugador set nombre=? where id=?', (pNombre, pId))
        miConexion.commit()
        miConexion.close()
        jugador,pos = self.buscarJugadorPorId(pId)
        if jugador != None:
            self.__jugadores[pos].setNombre(pNombre)
        #except Exception as e:
            #raise Exception('Hubo un error actualizando jugador: '+str(e))
    def buscarJugadorPorId(self,pId):
        '''()->Jugador Busca un jugador dado el id
        @:parameter pId id del jugador a buscar
        @:return Jugador devuelve un jugador None en caso contrario
        @:return posicion del jugador en el array'''
        i=0
        encontrado=False
        jugador=None
        while i< len(self.__jugadores) and not encontrado:
            if self.__jugadores[i].darId()==pId:
                encontrado=True
                jugador=self.__jugadores[i]
            i+=1
        return jugador,i-1
    def eliminarJugador(self,pId):
        '''()->void. Elimina un jugador de la base de datos
        @:parameter pId id del jugador a eliminar
        @:except Lanza una excepción si no logra eliminar'''
        try:
            miConexion = sqlite3.connect('../../data/bd/millonario.db')
            miCursor = miConexion.cursor()
            miCursor.execute('delete from jugador where id=?', (pId,))
            miConexion.commit()
            miConexion.close()
            jugador, pos = self.buscarJugadorPorId(pId)
            self.__jugadores.pop(pos)
        except Exception as e:
            raise Exception('Error eliminano: '+str(e))