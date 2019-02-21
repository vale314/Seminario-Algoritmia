from PySide2.QtWidgets import QMainWindow, QMessageBox,QFileDialog,QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from paquete import Paquete
from paqueteria import Paqueteria
from PySide2.QtGui import QPen, QColor,QBrush

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        self.paqueteria=Paqueteria()

        self.ui.pushButton.clicked.connect(self.click)
        self.ui.pushButton_2.clicked.connect(self.mostrar)
        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionAbrir.triggered.connect(self.abrir)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0,0,500,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0,0,0))
        self.pen.setWidth(30)

        self.scene.addLine(0,0,499,0,self.pen)
        self.scene.addLine(0,499,499,499,self.pen)
        self.scene.addLine(0,0,0,499,self.pen)
        self.scene.addLine(499,0,499,499,self.pen)

        self.pen.setColor(QColor(100,20,200))
        self.scene.addLine(10,10,490,490,self.pen)

        self.scene.addEllipse(10,10,5,5,self.pen,QBrush(QColor(50,100,0)))

        self.scene.addEllipse(490,490,5,5,self.pen,QBrush(QColor(50,100,0)))


    @Slot()
    def abrir(self):
        file = QFileDialog.getOpenFileName(self,'Abrir archivo','.','JSON(*.json)')
        self.paqueteria.recuperar(file[0])

    @Slot()
    def mostrar(self):
        #self.paqueteria.mostrar()
        for paquete in self.paqueteria.lista:
                self.ui.plainTextEdit.insertPlainText(str(paquete))

    @Slot()
    def guardar(self):
        file=QFileDialog.getSaveFileName(self,'Guardar Archivo...','.','JSON (*.json)')
        print(file)
        self.paqueteria.guardar(file[0])

    @Slot()
    def click(self):
        id=self.ui.lineEdit.text()
        origen=self.ui.lineEdit_2.text()
        destino=self.ui.lineEdit_3.text()
        distancia=self.ui.lineEdit_4.text()
        peso=self.ui.lineEdit_5.text()
        print(id, origen, destino, distancia, peso)

        paquete=Paquete()
        paquete.id= id
        paquete.origen=origen
        paquete.destino=destino
        paquete.distancia=distancia
        paquete.peso=peso

        self.paqueteria.agregar(paquete)

        msg=QMessageBox.information(self, 'Exito', 'Se agrego paquete con exito') #Ventana de mensaje de la libreria QMessageBox

        self.ui.lineEdit.clear()   #Limpiar campos
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
