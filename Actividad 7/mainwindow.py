from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from ui_mainwindow import  Ui_MainWindow
from PySide2.QtCore import Slot
from particula import Particula
from capturador import Capturador
from PySide2.QtWidgets import QMainWindow, QMessageBox,QFileDialog,QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor,QBrush

import math

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 500, 500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)



        self.capturador=Capturador()

        self.ui.pushButton.clicked.connect(self.click)
        self.ui.pushButton_2.clicked.connect(self.mostrar)

        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionAbrir_2.triggered.connect(self.abrir)

    @Slot()
    def guardar(self):

        file= QFileDialog.getSaveFileName(self, 'Guardar archivo...', '.', 'JSON (*.json)')
        print(file)
        self.capturador.guardar(file[0],self.pen,self.scene)

    @Slot()
    def abrir(self):
        file= QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'JSON (*.json)')
        self.capturador.recuperar(file[0])

    @Slot()
    def mostrar(self):
        self.scene.addLine(0, 0, 499, 0, self.pen)
        for particula in self.capturador.lista:
            self.ui.plainTextEdit.insertPlainText(str(particula))
            self.pen.setColor(QColor(particula.red, particula.green, particula.blue))
            self.scene.addLine(particula.origenX, particula.origenY, particula.destinoX, particula.destinoY, self.pen)
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