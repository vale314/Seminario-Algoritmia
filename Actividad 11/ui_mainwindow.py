# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Tue May 14 15:17:19 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 4, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 5, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 4, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 5, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 49, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(60, 20, 71, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 49, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 50, 71, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 49, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 80, 71, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(0, 110, 49, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 110, 71, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 24, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(60, 140, 71, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(140, 140, 51, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 140, 54, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(250, 140, 28, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(280, 140, 61, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(150, 40, 49, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(220, 40, 71, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(150, 80, 49, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(220, 80, 71, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 5)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 3, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 1, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 3, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 3, 5, 2)
        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 21))
        self.menubar.setObjectName("menubar")
        self.menusds = QtWidgets.QMenu(self.menubar)
        self.menusds.setObjectName("menusds")
        self.menuParticula = QtWidgets.QMenu(self.menubar)
        self.menuParticula.setObjectName("menuParticula")
        self.menuAlgoritmo = QtWidgets.QMenu(self.menubar)
        self.menuAlgoritmo.setObjectName("menuAlgoritmo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionAbrir_2 = QtWidgets.QAction(MainWindow)
        self.actionAbrir_2.setObjectName("actionAbrir_2")
        self.actionMostar = QtWidgets.QAction(MainWindow)
        self.actionMostar.setObjectName("actionMostar")
        self.actionPuntos_Cercanos = QtWidgets.QAction(MainWindow)
        self.actionPuntos_Cercanos.setObjectName("actionPuntos_Cercanos")
        self.actionkrustal = QtWidgets.QAction(MainWindow)
        self.actionkrustal.setObjectName("actionkrustal")
        self.actionDijkstra = QtWidgets.QAction(MainWindow)
        self.actionDijkstra.setObjectName("actionDijkstra")
        self.actionCamino_Dijkstra = QtWidgets.QAction(MainWindow)
        self.actionCamino_Dijkstra.setObjectName("actionCamino_Dijkstra")
        self.menusds.addAction(self.actionGuardar)
        self.menusds.addAction(self.actionAbrir_2)
        self.menuParticula.addAction(self.actionMostar)
        self.menuParticula.addAction(self.actionPuntos_Cercanos)
        self.menuAlgoritmo.addAction(self.actionkrustal)
        self.menuAlgoritmo.addSeparator()
        self.menuAlgoritmo.addAction(self.actionDijkstra)
        self.menuAlgoritmo.addAction(self.actionCamino_Dijkstra)
        self.menubar.addAction(self.menusds.menuAction())
        self.menubar.addAction(self.menuParticula.menuAction())
        self.menubar.addAction(self.menuAlgoritmo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.pushButton_8.setText(QtWidgets.QApplication.translate("MainWindow", "Prim", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "Ordenar Distancia", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "Grafo", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Ordenar Velocidad", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "ID:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Origen x:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Destino x:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Velocidad:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "RED:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "GREEN:", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "BLUE:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Origen y:", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Destino y:", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Agregar", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Mostrar", None, -1))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("MainWindow", "R.Anchura", None, -1))
        self.pushButton_10.setText(QtWidgets.QApplication.translate("MainWindow", "Dibujar Original", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "R.Profundidad", None, -1))
        self.pushButton_9.setText(QtWidgets.QApplication.translate("MainWindow", "Dibujar Prim", None, -1))
        self.menusds.setTitle(QtWidgets.QApplication.translate("MainWindow", "Archivo", None, -1))
        self.menuParticula.setTitle(QtWidgets.QApplication.translate("MainWindow", "Particula", None, -1))
        self.menuAlgoritmo.setTitle(QtWidgets.QApplication.translate("MainWindow", "Algoritmo", None, -1))
        self.actionGuardar.setText(QtWidgets.QApplication.translate("MainWindow", "Guardar", None, -1))
        self.actionGuardar.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.actionAbrir_2.setText(QtWidgets.QApplication.translate("MainWindow", "Abrir", None, -1))
        self.actionAbrir_2.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.actionMostar.setText(QtWidgets.QApplication.translate("MainWindow", "Mostar", None, -1))
        self.actionPuntos_Cercanos.setText(QtWidgets.QApplication.translate("MainWindow", "Puntos Cercanos", None, -1))
        self.actionkrustal.setText(QtWidgets.QApplication.translate("MainWindow", "krustkal", None, -1))
        self.actionDijkstra.setText(QtWidgets.QApplication.translate("MainWindow", "Dijkstra", None, -1))
        self.actionCamino_Dijkstra.setText(QtWidgets.QApplication.translate("MainWindow", "Camino Dijkstra", None, -1))

