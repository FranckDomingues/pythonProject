import sys
from PyQt5 import QtCore, QtWidgets, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtCore import QSize
from views.main_view_ui import Ui_MainWindow


class MainSimulator(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_ctrl = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        #self.setMinimumSize(QSize(640, 480))
        #self.setWindowTitle("Cisco Test - Simulator")

        # connect widgets to controller
        self._ui.pushButton_M1.clicked.connect(lambda: self._main_ctrl.def_method1())
        self._ui.pushButton_M2.clicked.connect(lambda: self._main_ctrl.def_method2())

        @pyqtSlot(str)
        def pybutton(self, value):
            self._ui.pushButton_M1.set
        QPushButton('Create Test', self)
        pybutton.resize(100, 32)
        pybutton.move(270, 120)
        pybutton.clicked.connect(self.clickMethod1)

        pybutton2 = QPushButton('Test', self)
        pybutton2.resize(100, 32)
        pybutton2.move(270, 240)
        pybutton2.clicked.connect(self.clickMethod2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Ui_MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
