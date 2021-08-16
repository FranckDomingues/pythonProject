from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtCore import QSize


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @pyqtSlot(str)
    def def_method1(self, value):
        self._model.method = value

        # definition buttons
        self._model.method1 = print('Clicked Pyqt button #1 Create. ')

    @pyqtSlot(str)
    def def_method2(self, value):
        self._model.method = value

        # definition buttons
        self._model.method2 = print('Clicked Pyqt button #2 Test. ')
        #from app import run_quiz
        #run_quiz()