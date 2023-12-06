import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

def func():
    mbox = QMessageBox()
    mbox.setText("setText")
    mbox.setDetailedText("detailed text")
    mbox.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
    mbox.exec_()


def application():
    app = QApplication(sys.argv)
    w=QWidget()
    w.resize(1400, 900)
    w.setWindowTitle("Otzovik")
    

    label = QLabel(w)
    label.setText("Label text")
    label.move(100,100)
    label.show

    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()

