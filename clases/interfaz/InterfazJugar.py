#Clase de la interfaz para las preguntas
from clases.interfaz.DialogoJugar import *
from PyQt5.QtWidgets import QDialog
class InterfazJugar(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
