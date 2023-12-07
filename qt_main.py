import sys
import os

from PyQt5.QtWidgets import *
# QApplication, QWidget, QLabel, QPushButton, QMessageBox, QGridLayout,QFileDialog, QScrollArea, SetWordWrap
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt

from exercises.exercise1 import task1
from exercises.exercise2 import task2
from exercises.exercise3 import task3
from exercises.exercise5 import otzovik


class Scroll(QScrollArea):
    def __init__(self, *args, **kwargs) -> None:
        QScrollArea.__init__(self, *args, **kwargs)
        self.setWidgetResizable(True)
        text = QWidget(self)
        self.setWidget(text)
        lay = QGridLayout(text)
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)
        self.label.setStyleSheet(
            "background: rgb(30,40,50); color: rgb(229, 220, 202); border: 5px, rgb(83,21,22);"
        )
        self.label.setFont(QFont("Times", 10))

    def setText(self, text: str) -> None:
        self.label.setText(text)


class window(QWidget):
    def __init__(self) -> None:
        super(QWidget, self).__init__()
        self.setFont(QFont("Times", 10))
        self.setStyleSheet("background: rgb(25,29,39); color: rgb(255,255,255)")

        self.dataset_button = QPushButton(self)
        self.dataset_button.setText("Укажите путь к dataset")
        self.dataset_button.adjustSize()
        self.dataset_button.clicked.connect(self.chose)
        self.dataset_button.setStyleSheet(
            "background: rgb(40,50,60); color: rgb(229, 220, 202);"
        )
        self.dataset_button.setFont(QFont("Times", 13))

        self.annotation_button = QPushButton(self)
        self.annotation_button.setText("Создать аннотацию к dataset")
        self.annotation_button.adjustSize()
        self.annotation_button.clicked.connect(self.create_anatation)
        self.annotation_button.setStyleSheet(
            "background: rgb(40,50,60); color: rgb(229, 220, 202);"
        )
        self.annotation_button.setFont(QFont("Times", 13))

        self.direct_button = QPushButton(self)
        self.direct_button.setText("Задать адрес сохранения копий")
        self.direct_button.adjustSize()
        self.direct_button.clicked.connect(self.get)
        self.direct_button.setStyleSheet(
            "background: rgb(40,50,60); color: rgb(229, 220, 202);"
        )
        self.direct_button.setFont(QFont("Times", 13))

        self.short_button = QPushButton(self)
        self.short_button.setText("Записать dataset в один файл")
        self.short_button.adjustSize()
        self.short_button.clicked.connect(self.short)
        self.short_button.setStyleSheet(
            "background: rgb(40,50,60); color: rgb(229, 220, 202);"
        )
        self.short_button.setFont(QFont("Times", 13))

        self.random_button = QPushButton(self)
        self.random_button.setText("Сделать dataset рандомным")
        self.random_button.adjustSize()
        self.random_button.clicked.connect(self.randam)
        self.random_button.setStyleSheet(
            "background: rgb(40,50,60); color: rgb(229, 220, 202);"
        )
        self.random_button.setFont(QFont("Times", 13))

        self.next_otzv = QPushButton(self)
        self.next_otzv.setText("Следующий отзыв ->")
        self.next_otzv.adjustSize()
        self.next_otzv.clicked.connect(self.next_o)
        self.next_otzv.setStyleSheet(
            "background: rgb(40,50,60); color: rgb(229, 220, 202);"
        )
        self.next_otzv.setFont(QFont("Times", 13))

        self.next_mark = QPushButton(self)
        self.next_mark.setText("Следующий рейтинг ->")
        self.next_mark.adjustSize()
        self.next_mark.clicked.connect(self.next_m)
        self.next_mark.setStyleSheet(
            "background: rgb(40,50,60); color: rgb(229, 220, 202);"
        )
        self.next_mark.setFont(QFont("Times", 13))

        self.review_lab = Scroll(self)
        self.review_lab.setText("Ожидание dataset'а...")

        self.star = QLabel(self)

        grid = QGridLayout(self)

        grid.addWidget(self.dataset_button, 1, 0)
        grid.addWidget(self.annotation_button, 2, 0)
        grid.addWidget(self.direct_button, 3, 0)
        grid.addWidget(self.short_button, 4, 0)
        grid.addWidget(self.random_button, 5, 0)
        grid.addWidget(self.next_otzv, 7, 4)
        grid.addWidget(self.next_mark, 7, 5)
        grid.addWidget(self.review_lab, 2, 2, 5, 6)
        grid.addWidget(self.star, 1, 2, 1, 6)

        self.setGeometry(0, 0, 1000, 1000)
        self.setWindowTitle("Otzovik")

    def chose(self) -> None:
        try:
            self.absolute = QFileDialog.getExistingDirectory(
                self, "Select Folder of datasset"
            )
            self.one = otzovik(self.absolute, "1")
            self.two = otzovik(self.absolute, "2")
            self.tree = otzovik(self.absolute, "3")
            self.four = otzovik(self.absolute, "4")
            self.five = otzovik(self.absolute, "5")
            self.count = 1
            self.next_o()
        except FileNotFoundError:
            QMessageBox.warning(
                self, "Внимание", "Неуказан путь dataset"
            )

    def next_o(self) -> None:
        try:
            if self.count == 1:
                f = open(next(self.one), "r", encoding="utf-8")
                otz = " ".join(f)
                self.review_lab.setText(otz)
                self.star.setText("Количество звёзд: ★")
            elif self.count == 2:
                f = open(next(self.two), "r", encoding="utf-8")
                otz = " ".join(f)
                self.review_lab.setText(otz)
                self.star.setText("Количество звёзд: ★★")
            elif self.count == 3:
                f = open(next(self.tree), "r", encoding="utf-8")
                otz = " ".join(f)
                self.review_lab.setText(otz)
                self.star.setText("Количество звёзд: ★★★")
            elif self.count == 4:
                f = open(next(self.four), "r", encoding="utf-8")
                otz = " ".join(f)
                self.review_lab.setText(otz)
                self.star.setText("Количество звёзд: ★★★★")
            elif self.count == 5:
                f = open(next(self.five), "r", encoding="utf-8")
                otz = " ".join(f)
                self.review_lab.setText(otz)
                self.star.setText("Количество звёзд: ★★★★★")
        except AttributeError:
            QMessageBox.warning(
                self, "Внимание", "Неуказан или указан неверно путь dataset"
            )

    def next_m(self):
        try:
            if self.count + 1 > 5:
                QMessageBox.warning(
                    self, "Внимание", "Достигнут лимит по рейтингу отзывов"
                )
                return
            else:
                self.count += 1
                self.next_o()
        except AttributeError:
            QMessageBox.warning(
                self, "Внимание", "Неуказан или указан неверно путь dataset"
            )

    def create_anatation(self) -> None:
        try:
            self.annatation = QFileDialog.getExistingDirectory(
                self, "Select Folder for annatation"
            )
            try:
                task1(self.absolute, self.annatation)
            except NotADirectoryError:
                QMessageBox.warning(
                    self, "Внимание", "Некоректный адрес dataset'а, введите новый"
                )
        except AttributeError:
            QMessageBox.warning(
                self, "Внимание", "Не указан или указан не верно путь dataset"
            )

    def get(self) -> None:
        self.new_path = QFileDialog.getExistingDirectory(
            self, "Select directory for copy"
        )

    def short(self) -> None:
        try:
            task2(self.absolute, self.new_path)
        except AttributeError:
            QMessageBox.warning(
                self, "Внимание", "Не указан путь для копирования или dataset"
            )

    def randam(self) -> None:
        try:
            task3(self.absolute, self.new_path)
        except AttributeError:
            QMessageBox.warning(
                self, "Внимание", "Не указан путь для копирования или dataset"
            )


def application():
    app = QApplication(sys.argv)
    main_window = window()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
