# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Sat Feb  9 00:45:12 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 274)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 4, 1, 2)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 6, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 4, 1, 2)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 2, 6, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 2, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 4, 3, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 5, 1, 2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 4, 7, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 5, 1, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 6, 1, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 455, 21))
        self.menubar.setObjectName("menubar")
        self.menusds = QtWidgets.QMenu(self.menubar)
        self.menusds.setObjectName("menusds")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionAbrir_2 = QtWidgets.QAction(MainWindow)
        self.actionAbrir_2.setObjectName("actionAbrir_2")
        self.menusds.addAction(self.actionGuardar)
        self.menusds.addAction(self.actionAbrir_2)
        self.menubar.addAction(self.menusds.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "ID:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Origen x:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Origen y:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Destino x:", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Destino y:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Velocidad:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "RED:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "GREEN:", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "BLUE:", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Agregar", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Distancia", None, -1))
        self.menusds.setTitle(QtWidgets.QApplication.translate("MainWindow", "Archivo", None, -1))
        self.actionGuardar.setText(QtWidgets.QApplication.translate("MainWindow", "Guardar", None, -1))
        self.actionGuardar.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.actionAbrir_2.setText(QtWidgets.QApplication.translate("MainWindow", "Abrir", None, -1))
        self.actionAbrir_2.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))

