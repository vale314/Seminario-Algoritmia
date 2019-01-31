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