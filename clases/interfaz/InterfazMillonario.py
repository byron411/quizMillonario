#Clase principal de la interfaz de usuario
from clases.interfaz.PanelMillonario import *
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys

class InterfazMillonario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=PanelMillonario()
        self.ui.setupUi(self)
app=QApplication([])
aplication=InterfazMillonario()
aplication.show()
sys.exit(app.exec())