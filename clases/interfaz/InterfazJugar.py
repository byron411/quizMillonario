#Clase de la interfaz para las preguntas
from clases.interfaz.DialogoJugar import *
from PyQt5.QtWidgets import QDialog,QMessageBox
import random
from clases.mundo.Millonario import *
class InterfazJugar(QDialog):
    def __init__(self,pNombre,pPreguntas,pRespuestas):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        '''Cargar nombre de jugador'''
        self.ui.lblNombre.setText('< html > < head / > < body > < p > < span style =\" font-size:12pt; font-weight:600; font-style:italic; color:#005500;\">'+pNombre+'</span></p></body></html>')
        self.nivel=1
        self.preguntas = pPreguntas
        self.respuestas=pRespuestas
        #print(len(self.respuestas))
        self.cargarPregunta()
        self.respuestas=pRespuestas
        '''confirmar'''
        self.ui.btnConfirmar.clicked.connect(self.confirmarRespuesta)

    def cargarPregunta(self):
        preguntasBasicas=[]
        if self.nivel==1:
            for i in range(len(self.preguntas)):
                if self.preguntas[i].darCategoria()=='bajo':
                    preguntasBasicas.append(self.preguntas[i])
            cantidadBasicas= len(preguntasBasicas)
            aleatorio=random.randint(0,cantidadBasicas-1)
            #print(str(cantidadBasicas)+' '+str(aleatorio))
            pregunta=preguntasBasicas[aleatorio]
            self.ui.textEditPregunta.setHtml("</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; \
            font-size:12pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; \
            margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aa00;\">"+str(pregunta)+"</span></p></body></html>")

            idRespuesta=preguntasBasicas[aleatorio].darIdRespuesta()
            self.cargarRespuesta(idRespuesta)

        else:
            pass

    def cargarRespuesta(self,pRespuesta):
        rbtnAleatorio=random.randint(1,4)
        principal=Millonario()
        respuesta=principal.buscarRespuestaPorId(pRespuesta)
        tipo=respuesta.darTipo()
        respuestasPorTipo=principal.buscarRespuestaPorTipo(tipo)

        des=respuesta.darDescripcion()
        for i in range(len(respuestasPorTipo)-1):
            if respuestasPorTipo[i].darDescripcion()==des:
                respuestasPorTipo.pop(i)

        if rbtnAleatorio==1:
            self.ui.rbtnA.setText(str(respuesta))
            self.ui.rbtnB.setText(str(respuestasPorTipo[0]))
            self.ui.rbtnC.setText(str(respuestasPorTipo[1]))
            self.ui.rbtnD.setText(str(respuestasPorTipo[2]))
        elif rbtnAleatorio==2:
            self.ui.rbtnA.setText(str(respuestasPorTipo[0]))
            self.ui.rbtnB.setText(str(respuesta))
            self.ui.rbtnC.setText(str(respuestasPorTipo[1]))
            self.ui.rbtnD.setText(str(respuestasPorTipo[2]))
        elif rbtnAleatorio==3:
            self.ui.rbtnA.setText(str(respuestasPorTipo[0]))
            self.ui.rbtnB.setText(str(respuestasPorTipo[1]))
            self.ui.rbtnC.setText(str(respuesta))
            self.ui.rbtnD.setText(str(respuestasPorTipo[2]))
        else:
            self.ui.rbtnA.setText(str(respuestasPorTipo[0]))
            self.ui.rbtnB.setText(str(respuestasPorTipo[1]))
            self.ui.rbtnC.setText(str(respuestasPorTipo[2]))
            self.ui.rbtnD.setText(str(respuesta))
    def confirmarRespuesta(self):
        respuesta=''
        princi=Millonario()
        if self.ui.rbtnA.isChecked():
            respuesta=self.ui.rbtnA.text()
        elif self.ui.rbtnB.isChecked():
            respuesta=self.ui.rbtnB.text()
        elif self.ui.rbtnC.isChecked():
            respuesta=self.ui.rbtnC.text()
        elif self.ui.rbtnD.isChecked():
            respuesta=self.ui.rbtnD.text()
        else:
            QMessageBox.warning(self,'Información','Debe seleccionar una respuesta')
        respuestaRecibida=princi.buscarRespuestaPorDescripcion(respuesta)

        if respuestaRecibida!=None:
            idRespuestaSeleccionada=respuestaRecibida.darId()
            preguntaRecibida=princi.buscarPreguntaPorIdRespuesta(idRespuestaSeleccionada)
            if preguntaRecibida!=None:
                QMessageBox.information(self,'Correcto','Es correcto pasa al siguiente nivel')
            else:
                QMessageBox.critical(self,'Incorrecto','Ha perdido su acumulado')