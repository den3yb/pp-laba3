import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QGridLayout,QFileDialog
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt

from exercises.exercise1 import task1
from exercises.exercise2 import task2

class window(QWidget):
    def __init__(self) -> None:
        super(QWidget,self).__init__()
        self.setFont(QFont("Times", 10))
        
        self.dataset_button = QPushButton(self)
        self.dataset_button.setText('Укажите путь к dataset')
        self.dataset_button.adjustSize()
        self.dataset_button.clicked.connect(self.chose)
        #self.dataset_button.setStyleSheet("QPushButton {background-color: rgb(67,124,144), color: rgb(250, 131,52)}")
        
        

        self.annotation_button = QPushButton(self)
        self.annotation_button.setText('Создать аннотацию к dataset')
        self.annotation_button.adjustSize()
        self.annotation_button.clicked.connect(self.create_anatation)

       

        self.direct_button = QPushButton(self)
        self.direct_button.setText('Задать адрес сохранения копий')
        self.direct_button.adjustSize()
        self.direct_button.clicked.connect(self.get)
        

        self.short_button = QPushButton(self)
        self.short_button.setText('Записать dataset в один файл')
        self.short_button.adjustSize()
        self.short_button.clicked.connect(self.short)
        
        

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

        #qp=QPalette()
        #qp.setColor(QPalette.Window, QColor(45,45,45))
        #qp.setColor(QPalette.Button, QColor(67,124,144))
        #qp.setColor(QPalette.ButtonText, QColor(250,131,52))
        #self.setPalette(qp)
        
        grid = QGridLayout(self)
        grid.setSpacing(6)
        grid.addWidget(self.dataset_button,0,1)
        grid.addWidget(self.annotation_button,1,1)
        grid.addWidget(self.direct_button,3,1)
        grid.addWidget(self.short_button,4,1)
        grid.addWidget(self.random_button,5,1)
        grid.addWidget(self.next_otzv,6,3)
        grid.addWidget(self.next_mark,6,4)
        grid.addWidget(self.review_lab,0,2,3,4)

        self.setGeometry(0,0,1200,900)
        self.setWindowTitle("Otzovik")


    def chose(self) -> None:
        self.absolute = QFileDialog.getExistingDirectory(self, 'Select Folder of datasset')



    def create_anatation(self) -> None:
        self.annatation = QFileDialog.getExistingDirectory(self, 'Select Folder for annatation')
        try:
            task1(self.absolute, self.annatation)
        except NotADirectoryError:
            print ("Некоректный адрес dataset, введите новый")



    def get(self) -> None:
        self.new_path = QFileDialog.getExistingDirectory(self, 'Select directory for copy')




    def short(self) -> None:
        try:
            task2(self.absolute, self.new_path)
        except AttributeError:
            print ("Сначала укажите путь сохранения")

        
        
        
def application():
   app = QApplication (sys.argv)
   main_window = window()
   main_window.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
    application()

