from PyQt5.QtCore import QObject #, pyqtSignal

class Model(QObject):

    @property
    def m1(self):
        return self._m1

    @m1.setter
    def m1(self, value):
        self._m1 = value
        self.de
