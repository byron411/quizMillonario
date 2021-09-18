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
            pregunta=preguntasBasicas[aleatorio]
            self.ui.textEditPregunta.setHtml("</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; \
            font-size:12pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; \
            margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aa00;\">"+str(pregunta)+"</span></p></body></html>")

            idRespuesta=preguntasBasicas[aleatorio].darIdRespuesta()
            self.cargarRespuesta(idRespuesta)

        elif self.nivel==2:
            preguntas_medio_bajo = []
            for j in range(len(self.preguntas)):
                if self.preguntas[j].darCategoria()=='medio_bajo':
                    preguntas_medio_bajo.append(self.preguntas[j])
            cantidad_medio_bajo= len(preguntas_medio_bajo)
            aleatorio2=random.randint(0,cantidad_medio_bajo-1)
            pregunta2=preguntas_medio_bajo[aleatorio2]
            self.ui.textEditPregunta.setHtml("</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; \
                        font-size:12pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; \
                        margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aa00;\">" + str(pregunta2) + "</span></p></body></html>")
            idRespuesta2=preguntas_medio_bajo[aleatorio2].darIdRespuesta()
            self.cargarRespuesta(idRespuesta2)

        elif self.nivel==3:
            preguntas_medias = []
            for k in range(len(self.preguntas)):
                if self.preguntas[k].darCategoria()=='medio':
                    preguntas_medias.append(self.preguntas[k])
            cantidad_medio= len(preguntas_medias)
            aleatorio3=random.randint(0,cantidad_medio-1)
            pregunta3=preguntas_medias[aleatorio3]
            self.ui.textEditPregunta.setHtml("</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; \
                        font-size:12pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; \
                        margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aa00;\">" + str(pregunta3) + "</span></p></body></html>")
            idRespuesta3=preguntas_medias[aleatorio3].darIdRespuesta()
            self.cargarRespuesta(idRespuesta3)

        elif self.nivel==4:
            preguntas_medias_altas = []
            for h in range(len(self.preguntas)):
                if self.preguntas[h].darCategoria()=='medio_alto':
                    preguntas_medias_altas.append(self.preguntas[h])
            cantidad_medias_altas= len(preguntas_medias_altas)
            aleatorio4=random.randint(0,cantidad_medias_altas-1)
            pregunta4=preguntas_medias_altas[aleatorio4]
            self.ui.textEditPregunta.setHtml("</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; \
                        font-size:12pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; \
                        margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aa00;\">" + str(pregunta4) + "</span></p></body></html>")
            idRespuesta4=preguntas_medias_altas[aleatorio4].darIdRespuesta()
            self.cargarRespuesta(idRespuesta4)

        elif self.nivel==5:
            preguntas_altas=[]
            for t in range(len(self.preguntas)):
                if self.preguntas[t].darCategoria()=='alto':
                    preguntas_altas.append(self.preguntas[t])
            cantidad_altas= len(preguntas_altas)
            aleatorio5=random.randint(0,cantidad_altas-1)
            pregunta5=preguntas_altas[aleatorio5]
            self.ui.textEditPregunta.setHtml("</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; \
                                    font-size:12pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; \
                                    margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aa00;\">" + str(pregunta5) + "</span></p></body></html>")
            idRespuesta5 = preguntas_altas[aleatorio5].darIdRespuesta()
            self.cargarRespuesta(idRespuesta5)



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
                self.nivel+=1
                self.cargarPregunta()
            else:
                QMessageBox.critical(self,'Incorrecto','Ha perdido su acumulado')