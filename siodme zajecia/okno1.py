import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from qt import MyWindow


class Okno1(QDialog):
    def __init__(self):
        super(Okno1,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 900, 900) #od lewej od gory szerokosc wysokosc
        self.setWindowTitle("zadanie 7 Witold Kardas")

        self.b1 = QPushButton(self)
        self.b1.setText("Wróć kurwa")
        self.b1.clicked.connect(self.goMainWindow)
        self.b1.setGeometry(10, 10, 250, 50)

    def goMainWindow(self):
        self.cams = MyWindow()
        self.cams.show()
        self.close() 

    def update(self):
        self.label.adjustSize()

