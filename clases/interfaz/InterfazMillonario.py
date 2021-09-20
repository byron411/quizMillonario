#Clase principal de la interfaz de usuario
from clases.interfaz.PanelMillonario import *
from PyQt5.QtWidgets import QMainWindow,QApplication,QInputDialog
#from clases.mundo.Millonario import *
from clases.interfaz.InterfazJugar import *
import sys
class InterfazMillonario(QMainWindow):
    def __init__(self):
        super().__init__()
        '''crea un objeto al panel principla'''
        self.ui=PanelMillonario()
        self.ui.setupUi(self)
        '''crea una instancia a la clase principal'''
        self.principal=Millonario()
        self.jugadores=self.principal.darJugadores()
        '''cargar jugadores'''
        self.cargarJugadores()
        '''botones'''
        self.ui.btnAgregar.clicked.connect(self.agregarJugador)
        '''Selección de socios con mouse'''
        self.ui.listWidgetJugadores.itemClicked.connect(self.refrescarGroupBox)
        self.ui.listWidgetJugadores.itemSelectionChanged.connect(self.refrescarGroupBox)
        '''boton ¡Jugar!'''
        self.ui.btnJugar.clicked.connect(self.jugar)
        '''preguntas'''
        self.preguntas=self.principal.darPreguntas()
        '''respuestas'''
        self.respuestas=self.principal.darRespuestas()
        '''menú salir'''
        self.ui.actionSalir.triggered.connect(self.salir)
        '''Actualizar group box'''
        self.ui.btnRefrescar.clicked.connect(self.refrescarGroupBox)
        '''menú ayuda'''
        self.ui.actionInstrucciones.triggered.connect(self.instrucciones)
        '''menú programador'''
        self.ui.actionProgramador.triggered.connect(self.programador)
        '''actualizar jugador'''
        self.ui.actionModificar_jugador_seleccionado.triggered.connect(self.actualizarJugador)
        '''eliminar usuario'''
        self.ui.actionEliminar_jugador_seleccionado.triggered.connect(self.eliminarJugador)
        '''buscar usuario'''
        self.ui.actionBuscar_jugador.triggered.connect(self.buscarJugador)
    def cargarJugadores(self):
        '''Carga los jugadores de la base de datos en el widget
        @:except Lanza una excepción si no logra encontrar jugadores'''
        try:
            for i in range(len(self.jugadores)):
                self.ui.listWidgetJugadores.addItem(str(self.jugadores[i]))
            self.ui.listWidgetJugadores.setCurrentRow(0)
            self.mostrarJugadorActual()
        except Exception as e:
            QMessageBox.critical(self,'Error',str(e))
    def agregarJugador(self):
        '''Solicita un nombre de jugador, valida la información y solicita guardarlo, refrescarlo y mostrarlo
           @:except Lanza una excepción si no encuentra la base de datos'''
        nombre,boleano=QInputDialog.getText(self,'Agregar jugador','Nombre completo:')
        nom=nombre.strip()
        if boleano:
            if nom!='':
                try:
                    self.principal.agregarJugador(nom)
                    self.refrescarJugadores()
                    self.mostrarJugadorActual()
                    QMessageBox.information(self,'Jugador agregado','Se ha agregado al jugador con éxito')
                except Exception as e:
                    QMessageBox.critical(self,'Error',str(e))
            else:
                QMessageBox.warning(self,'Sin nombre','Debe ingresar un nombre')
    def refrescarJugadores(self):
        '''Actualiza el widget de los jugadores'''
        jugadores=self.principal.darJugadores()
        self.ui.listWidgetJugadores.clear()
        for i in range(len(jugadores)):
            self.ui.listWidgetJugadores.addItem(str(jugadores[i].darNombre()))
        self.ui.listWidgetJugadores.setCurrentRow(i)
    def mostrarJugadorActual(self):

        if len(self.jugadores)>0:
            item=self.ui.listWidgetJugadores.currentRow()
            self.ui.txtNombre.setText(self.jugadores[item].darNombre())
            self.ui.txtAcumulado.setText(str('${:,.2f}'.format(self.jugadores[item].darAcumulado())))
            self.ui.txtJugados.setText(str(self.jugadores[item].darJugados()))
            self.ui.txtGanados.setText(str(self.jugadores[item].darGanados()))
            self.ui.txtPerdidos.setText(str(self.jugadores[item].darPerdidos()))
            self.ui.txtRetirados.setText(str(self.jugadores[item].darRetirados()))

    def jugar(self):
        item=self.ui.listWidgetJugadores.currentRow()
        if item>=0:
            nombre=self.jugadores[item].darNombre()
            dialogoJugar=InterfazJugar(nombre,self.preguntas,self.respuestas)
            dialogoJugar.exec()

        else:
            QMessageBox.warning(self,'Sin jugadores','No hay jugadores puede agregarlo en el botón Agregar Jugador de la pantalla principal')

    def refrescarGroupBox(self):
        '''Muestra la información del jugador actual en el groupBox Jugador actual'''
        pri=Millonario()
        lista=pri.darJugadores()
        if len(lista)>0:
            item=self.ui.listWidgetJugadores.currentRow()
            try:
                self.ui.txtNombre.setText(lista[item].darNombre())
                self.ui.txtAcumulado.setText(str('${:,.2f}'.format(lista[item].darAcumulado())))
                self.ui.txtJugados.setText(str(lista[item].darJugados()))
                self.ui.txtGanados.setText(str(lista[item].darGanados()))
                self.ui.txtPerdidos.setText(str(lista[item].darPerdidos()))
                self.ui.txtRetirados.setText(str(lista[item].darRetirados()))
            except Exception as e:
                pass
    def salir(self):
        self.msg = QMessageBox.question(self, 'Confirmación',
                                                  '¿Desea salir?',
                                                  QMessageBox.Yes | QMessageBox.No)
        if self.msg == QMessageBox.Yes:
            sys.exit(app.exec())
    def instrucciones(self):
        '''Muestra un mensaje de instrucciones'''
        QMessageBox.information(self,'Instrucciones','Agregue un jugador y presione el botón jugar.\n'
        'Responda 5 preguntas cada una con un valor diferente.\nCuenta con 3 ayudas solo se utilizan una vez.\n'
        'Si se retira despues de la primera pregunta conserva su acumulado.\nSi contesta mal perderá su acumulado.')
    def programador(self):
        '''Muestra un mensaje de la persona que realizó el programa'''
        QMessageBox.information(self,'Programador','Bayron Trejo\nCel. 3153040495\nEmail. brntrj@gmail.com')
    def actualizarJugador(self):
        item=self.ui.listWidgetJugadores.currentRow()
        if item>=0:
            nombre,boolenao=QInputDialog.getText(self,'Nuevo nombre','Ingrese el nuevo nombre:')
            nom=nombre.strip()
            if boolenao:
                if nom!='':
                    try:
                        pid=self.jugadores[item].darId()
                        self.principal.actualizarJugador(nom,pid)
                        self.ui.listWidgetJugadores.clear()
                        self.refrescarJugadores()
                        self.mostrarJugadorActual()
                        self.ui.listWidgetJugadores.setCurrentRow(item)
                        QMessageBox.information(self,'Actualizado','Se ha actualizado el jugador')
                    except Exception as e:
                        QMessageBox.critical(self,'Error','Error actualizando jugador '+str(e))
                else:
                    QMessageBox.critical(self,'Error','Debe ingresar un nombre')
    def eliminarJugador(self):
        '''elimina un jugador'''
        item=self.ui.listWidgetJugadores.currentRow()
        if item>=0:
            self.msg = QMessageBox.question(self, 'Confirmación',
                                            '¿Eliminar a '+str(self.jugadores[item].darNombre())+'?',
                                            QMessageBox.Yes | QMessageBox.No)
            if self.msg == QMessageBox.Yes:
                try:
                    self.principal.eliminarJugador(self.jugadores[item].darId())
                    self.refrescarJugadores()
                    self.mostrarJugadorActual()
                    if len(self.jugadores)>0:
                        self.ui.listWidgetJugadores.setCurrentRow(0)
                    else:
                        pass
                except Exception as e:
                    QMessageBox.critical(self,'Error','Error eliminando jugador '+str(e))
    def buscarJugador(self):
        '''busca un jugador'''
        jugadores= len(self.jugadores)
        if jugadores>=0:

            nombre,booleano=QInputDialog.getText(self,'Buscar','Ingrese nombre:')
            nom=nombre.strip()
            if booleano:
                if nom!='':
                    jugador=self.principal.buscarJugadorPorNombre(nom)
                    if jugador!=None:
                        jugadorpor,posicion=self.principal.buscarJugadorPorId(jugador.darId())
                        if jugadorpor!=None:
                            self.ui.listWidgetJugadores.setCurrentRow(posicion)
                            QMessageBox.information(self,'Encontrado','Jugador '+str(jugadorpor.darNombre()+'esta en la posición '+str(posicion)))
                    else:
                        QMessageBox.information(self,'NO esta','No se ha encontrado el jugador')
                else:
                    QMessageBox.warning(self,'Error','No ha ingresado un nombre de jugador')


app=QApplication([])
aplication=InterfazMillonario()
aplication.show()
sys.exit(app.exec())