# pip install -r requirements.txt
# convertion ui to python pyside2-uic origen.ui > ui_destino.py



import sys
from PySide2.QtWidgets import  QApplication, QLabel
from mainwindow import  MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app = QApplication(sys.argv)
    # label = QLabel("Hello World")
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())