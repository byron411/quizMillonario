#Clase principal de la interfaz de usuario
from clases.interfaz.PanelMillonario import *
from PyQt5.QtWidgets import QMainWindow,QApplication,QInputDialog,QMessageBox
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
        self.ui.listWidgetJugadores.itemClicked.connect(self.mostrarJugadorActual)
        self.ui.listWidgetJugadores.itemSelectionChanged.connect(self.mostrarJugadorActual)
        '''boton ¡Jugar!'''
        self.ui.btnJugar.clicked.connect(self.jugar)
        '''preguntas'''
        self.preguntas=self.principal.darPreguntas()
        '''respuestas'''
        self.respuestas=self.principal.darRespuestas()
        #print(len(self.respuestas))

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
        self.ui.listWidgetJugadores.clear()
        for i in range(len(self.jugadores)):
            self.ui.listWidgetJugadores.addItem(str(self.jugadores[i]))
        self.ui.listWidgetJugadores.setCurrentRow(i)
    def mostrarJugadorActual(self):
        '''Muestra la información del jugador actual en el groupBox Jugador actual'''
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


app=QApplication([])
aplication=InterfazMillonario()
aplication.show()
sys.exit(app.exec())