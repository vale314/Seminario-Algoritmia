from PySide2.QtCore import Slot
from particula import Particula
from capturador import Capturador
from PySide2.QtWidgets import QMainWindow, QMessageBox,QFileDialog,QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor,QBrush
import json
#https://www.geeksforgeeks.org/python-program-for-bubble-sort/
import math

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        #self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)


        self.lista=[];
        self.listaMenor=[];

        self.capturador=Capturador()

        self.ui.pushButton.clicked.connect(self.click)
        self.ui.pushButton_2.clicked.connect(self.mostrar)

        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionAbrir_2.triggered.connect(self.abrir)
        self.ui.actionMostar.triggered.connect(self.mostarParticulasPuntos)

        self.ui.actionPuntos_Cercanos.triggered.connect(self.puntos_cercanos)

        self.ui.pushButton_3.clicked.connect(self.ordenar_velocidad)

        self.ui.pushButton_4.clicked.connect(self.ordenar_distancia)

    @Slot()
    def puntos_cercanos(self):
        i=0;
        for particula in self.lista:
            particulaMenor=particula[i+1];
            i=i+1;
            for particula2 in self.lista:
                if(math.sqrt(pow((int(particula2.destinoX)-int(particula2.origenX)),2)+pow((int(particulaMenor.destinoY)-int(particulaMenor.origenY)),2))<math.sqrt(pow((int(particula2.destinoX)-int(particula2.origenX)),2)+pow((int(particula2.destinoY)-int(particula2.origenY)),2)))
                print (particulaMenor,particula2)

    @Slot()
    def mostarParticulasPuntos(self):
        self.scene.clear()
        self.scene = QGraphicsScene()
        # self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)
        self.capturador.ordenar_velocidad()
        for particula in self.capturador.lista:
            self.lista.append({
                'x':particula.origenX,
                'y':particula.origenY,
                'color':{
                    'red':particula.red,
                    'green':particula.green,
                    'blue':particula.blue
                }
            })
            self.lista.append({
                'x':particula.destinoX,
                'y':particula.destinoY,
                'color':{
                    'red':particula.red,
                    'green':particula.green,
                    'blue':particula.blue
                }
            })
            self.ui.plainTextEdit.insertPlainText(str(particula))
            self.pen.setColor(QColor(particula.red, particula.green, particula.blue))
            self.scene.addEllipse(particula.origenX, particula.origenY, 5, 5, self.pen, QBrush(QColor(particula.red, 10,particula.green, particula.blue)))

    @Slot()
    def ordenar_velocidad(self):
        self.scene.clear()
        self.scene = QGraphicsScene()
        #self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)
        self.capturador.ordenar_velocidad()
        y=0
        for particula in self.capturador.lista:
            self.ui.plainTextEdit.insertPlainText(str(particula))
            self.pen.setColor(QColor(particula.red, particula.green, particula.blue))
            self.scene.addLine(0, y, particula.distancia, y, self.pen)
            y=y+2

    @Slot()
    def ordenar_distancia(self):
        self.scene.clear()
        self.scene = QGraphicsScene()
        #self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)
        self.capturador.ordenar_distancia()
        y=0
        for particula in self.capturador.lista:
            self.ui.plainTextEdit.insertPlainText(str(particula))
            self.pen.setColor(QColor(particula.red, particula.green, particula.blue))
            self.scene.addLine(0, y, particula.distancia, y, self.pen)
            y=y+2


    @Slot()
    def guardar(self):
        self.scene = QGraphicsScene()
        #self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)
        file= QFileDialog.getSaveFileName(self, 'Guardar archivo...', '.', 'JSON (*.json)')
        print(file)
        self.capturador.guardar(file[0],self.pen,self.scene)

    @Slot()
    def abrir(self):
        file= QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'JSON (*.json)')
        self.capturador.recuperar(file[0])

    @Slot()
    def mostrar(self):
        self.scene.clear()
        self.scene.addLine(0, 0, 499, 0, self.pen)
        y=0
        for particula in self.capturador.lista:
            self.ui.plainTextEdit.insertPlainText(str(particula))
            self.pen.setColor(QColor(particula.red, particula.green, particula.blue))
            self.scene.addLine(0, y, particula.distancia, y, self.pen)
            y=y+2
        #for particula in self.capturador.lista:
         #   self.ui.plainTextEdit.insertPlainText(str(particula))
          #  self.pen.setColor(QColor(particula.red, particula.green, particula.blue))
           # self.scene.addEllipse(particula.origenX, particula.origenY, 5, 5, self.pen, QBrush(QColor(particula.red, 10,particula.green, particula.blue)))
            #self.scene.addLine(particula.origenX, particula.origenY, particula.destinoX, particula.destinoY, self.pen)
        #self.paqueteria.mostrar()

    @Slot()
    def click(self):

        id=self.ui.lineEdit.text()
        origenX=self.ui.lineEdit_2.text()
        origenY=self.ui.lineEdit_6.text()
        destinoX=self.ui.lineEdit_3.text()
        destinoY=self.ui.lineEdit_7.text()
        velocidad=self.ui.lineEdit_4.text()
        red=self.ui.lineEdit_5.text()
        green=self.ui.lineEdit_8.text()
        blue=self.ui.lineEdit_9.text()

        print(id, origenX, origenY,destinoX, destinoY, velocidad, red, green, blue)

        partiula=Particula()
        partiula.id= id
        partiula.origenX=int(origenX)
        partiula.origenY=int(origenY)
        partiula.destinoX=int(destinoX)
        partiula.destinoY=int(destinoY)
        partiula.distancia=math.sqrt(pow((int(destinoX)-int(origenX)),2)+pow((int(destinoY)-int(origenY)),2))
        partiula.red=int(red)
        partiula.green=int(green)
        partiula.blue=int(blue)
        partiula.velocidad=int(velocidad)


        self.capturador.agregar(partiula)

        msg=QMessageBox.information(self, 'Exito', 'Se agrego paquete con exito') #Ventana de mensaje de la libreria QMessageBox

        self.ui.lineEdit.clear()   #Limpiar campos
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_9.clear()