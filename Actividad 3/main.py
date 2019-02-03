# pip install -r requirements.txt
# convertion ui to python pyside2-uic origen.ui > ui_destino.py  # pip freeze > requirements.txt

import sys
from PySide2.QtWidgets import QApplication, QLabel
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # label = QLabel("Hello World")
    # label.show()
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())