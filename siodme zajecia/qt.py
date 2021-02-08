import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from funkcjaLiniowa import funkcjaLiniowa
from funkcjaKwadratowa import funkcjaKwadratowa
from zbiorFunkcji import zbiorFunkcji
from wykresFunkcji import wykresFunkcji
from Menu import display_menu,display_remove_function_menu_2, display_add_function_menu, display_remove_function_menu, return_new_float_value_or_previous_one, return_not_empty_new_string_or_previous_one

#from okno1 import Okno1
zbior_funkcji = zbiorFunkcji()
wykresy_funkcji = wykresFunkcji(zbior_funkcji)
x_min = -10
x_max = 10
y_min = None
y_max = None
step = 0.0001
file_name = "data.dat"

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button3_clicked(self):
        wykresy_funkcji._show_plot()

    def button4_clicked(self):
        #not yet
        print("not yet")

    def button5_clicked(self):
        wykresy_funkcji.plot()

    def button6_clicked(self):
        zbior_funkcji.save_to_file("data.dat")

    def button7_clicked(self):
        zbior_funkcji.read_from_file("data.dat")

    def button8_clicked(self):
        quit()

    def initUI(self):
        self.setGeometry(300, 300, 900, 900) #od lewej od gory szerokosc wysokosc
        self.setWindowTitle("zadanie 7 Witold Kardas")

        self.b1 = QPushButton(self)
        self.b1.setText("Dodanie funkcji")
        self.b1.clicked.connect(self.button1_clicked)
        self.b1.setGeometry(10, 10, 250, 50)

        self.b2 = QPushButton(self)
        self.b2.setText("Usuniecie funkcji")
        self.b2.clicked.connect(self.button2_clicked)
        self.b2.setGeometry(10, 80, 250, 50)

        self.b3 = QPushButton(self)
        self.b3.setText("Wyswietlenie funkcji")
        self.b3.clicked.connect(self.button3_clicked)
        self.b3.setGeometry(10, 150, 250, 50)

        self.b4 = QPushButton(self)
        self.b4.setText("Definiowanie parametrow wykresu funkcji")
        self.b4.clicked.connect(self.button4_clicked)
        self.b4.setGeometry(10, 220, 250, 50)

        self.b5 = QPushButton(self)
        self.b5.setText("Generowanie wykresu funkcji")
        self.b5.clicked.connect(self.button5_clicked)
        self.b5.setGeometry(10, 290, 250, 50)

        self.b6 = QPushButton(self)
        self.b6.setText("Zapisanie zbioru funkcji do pliku")
        self.b6.clicked.connect(self.button6_clicked)
        self.b6.setGeometry(10, 360, 250, 50)

        self.b7 = QPushButton(self)
        self.b7.setText("Odczytanie zbioru funkcji z pliku")
        self.b7.clicked.connect(self.button7_clicked)
        self.b7.setGeometry(10, 430, 250, 50)

        self.b8 = QPushButton(self)
        self.b8.setText("Koniec programu")
        self.b8.clicked.connect(self.button8_clicked)
        self.b8.setGeometry(10, 500, 250, 50)

    @pyqtSlot()
    def button1_clicked(self):
        self.cams = Okno1() 
        self.cams.show()
        self.close()

    @pyqtSlot()
    def button2_clicked(self):
        self.cams = Okno2() 
        self.cams.show()
        self.close()


#================ OKNO DODAWANIA FUNKCJI ====================

class Okno1(QDialog):
    def __init__(self):
        super(Okno1,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 900, 900) #od lewej od gory szerokosc wysokosc
        self.setWindowTitle("zadanie 7 Witold Kardas")

        self.b1 = QPushButton(self)
        self.b1.setText("Dodaj wpisane funkcje")
        self.b1.clicked.connect(self.AddFunction)
        self.b1.setGeometry(10, 10, 250, 50)

        self.b2 = QPushButton(self)
        self.b2.setText("Wróć")
        self.b2.clicked.connect(self.goMainWindow)
        self.b2.setGeometry(10, 80, 250, 50)

        font = QFont()
        font.setPointSize(15)

        self.label = QLabel(self)
        self.label.setText("Wartość a:")
        self.label.setGeometry(300, 10, 80, 50)

        self.label = QLabel(self)
        self.label.setText("Wartość b:")
        self.label.setGeometry(420, 10, 80, 50)

        self.label = QLabel(self)
        self.label.setText("Wartość c:")
        self.label.setGeometry(540, 10, 80, 50)

        self.a_input = QLineEdit(self)
        self.a_input.setFont(font)
        self.a_input.setGeometry(300, 80, 100, 50)

        self.b_input = QLineEdit(self)
        self.b_input.setFont(font)
        self.b_input.setGeometry(420, 80, 100, 50)

        self.c_input = QLineEdit(self)
        self.c_input.setFont(font)
        self.c_input.setGeometry(540, 80, 100, 50)

    def goMainWindow(self):
        self.cams = MyWindow()
        self.cams.show()
        self.close() 

    def AddFunction(self):
        if self.a_input.text() == '':
            a = 0
            b = int(self.b_input.text())
            c = int(self.c_input.text())
        else:
            a = int(self.a_input.text())
            b = int(self.b_input.text())
            c = int(self.c_input.text())

        if a:
            funkcja = funkcjaKwadratowa.create_function(a=a, b=b, c=c)
            zbior_funkcji.add_function(funkcja)
        else:
            funkcja = funkcjaLiniowa.create_function(a=b, b=c)
            zbior_funkcji.add_function(funkcja)


    def update(self):
        self.label.adjustSize()


#=========== OKNO USUWANIA ====================

class Okno2(QDialog):
    def __init__(self):
        super(Okno2,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 900, 900) #od lewej od gory szerokosc wysokosc
        self.setWindowTitle("zadanie 7 Witold Kardas")

        self.b1 = QPushButton(self)
        self.b1.setText("Usun podana funkcje")
        self.b1.clicked.connect(self.RmFunction)
        self.b1.setGeometry(10, 10, 250, 50)

        self.b2 = QPushButton(self)
        self.b2.setText("Wróć")
        self.b2.clicked.connect(self.goMainWindow)
        self.b2.setGeometry(10, 80, 250, 50)

        font = QFont()
        font.setPointSize(15)

        self.label = QLabel(self)
        self.label.setText("Podaj index funkcji do usuniecia")
        self.label.setGeometry(300, 10, 80, 50)

        self.a_input = QLineEdit(self)
        self.a_input.setFont(font)
        self.a_input.setGeometry(300, 80, 100, 50)

    def goMainWindow(self):
        self.cams = MyWindow()
        self.cams.show()
        self.close() 

    def RmFunction(self):
        index = int(self.a_input.text())
        zbior_funkcji.delete_function_by(index-1)

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()