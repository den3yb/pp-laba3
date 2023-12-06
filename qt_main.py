import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QGridLayout
from PyQt5.QtGui import QPalette, QColor


class window(QWidget):
    def __init__(self) -> None:
        super(QWidget,self).__init__()
        
        self.dataset_button = QPushButton(self)
        self.dataset_button.setText('Укажите путь к dataset')
        self.dataset_button.adjustSize()

        self.annotation_button = QPushButton(self)
        self.annotation_button.setText('Создать аннотацию к dataset')
        self.annotation_button.adjustSize()
       

        self.short_button = QPushButton(self)
        self.short_button.setText('Записать dataset в один файл')
        self.short_button.adjustSize()
        

        self.random_button = QPushButton(self)
        self.random_button.setText('Сделать dataset рандомным')
        self.random_button.adjustSize()
        

        self.next_otzv = QPushButton(self)
        self.next_otzv.setText('Следующий отзыв ->')
        self.next_otzv.adjustSize()
        

        self.next_mark = QPushButton(self)
        self.next_mark.setText('Следующая оценка ->')
        self.next_mark.adjustSize()
        

        self.review_lab = QLabel(self)
        self.review_lab.setText("")
        self.review_lab.adjustSize()
        
        
        grid = QGridLayout(self)
        grid.setSpacing(6)
        grid.addWidget(self.dataset_button,0,1)
        grid.addWidget(self.annotation_button,1,1)
        grid.addWidget(self.short_button,4,1)
        grid.addWidget(self.random_button,5,1)
        grid.addWidget(self.next_otzv,6,3)
        grid.addWidget(self.next_mark,6,4)
        grid.addWidget(self.review_lab,0,2,3,4)

        self.setGeometry(0,0,1200,900)
        self.setWindowTitle("Otzovik")

       


        
        
        
def application():
   app = QApplication (sys.argv)
   main_window = window()
   main_window.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
    application()

