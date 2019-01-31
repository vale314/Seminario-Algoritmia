from PySide2.QtWidgets import QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from paquete import Paquete
from paqueteria import Paqueteria

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        self.paqueteria=Paqueteria()

        self.ui.pushButton.clicked.connect(self.click)
        self.ui.pushButton_2.clicked.connect(self.mostrar)

    @Slot()
    def mostrar(self):
        self.paqueteria.mostrar()

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
        self.ui.lineEdit_5.clear()s