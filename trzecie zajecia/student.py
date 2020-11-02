import pickle


class Student:
    def __init__(self, name, surname, index_nmber, rating_list=[]):
        self.__name = name
        self.__surname = surname
        self.__index_number = index_nmber
        self.__rating_list = rating_list[:]

    def show(self):
        print(f"Student: {self.__name} {self.__surname}")
        print(f"Index Number: {self.__index_number}")
        print(f"Rating list: {self.__rating_list}")

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_index_nmber(self, index_nmber):
        self.__index_number = index_nmber

    def avg_rating(self):
        return sum(self.__rating_list) / len(self.__rating_list)

    def show_rating(self):
        print(self.__rating_list)

    def change_grades(self):
        print("Dodac czy usunac oceny? [d/u]")
        x = input()

        if x == "d":
            print("Jaka ocene dodac?")
            d = int(input())
            self.__rating_list.append(d)
        if x == "u":
            print("Ktora ocene usunac?")
            d = int(input())
            self.__rating_list.pop(d-1)


def defense_int_input(text, min_val, max_val):
    value = input(text)
    while ((int(min_val) > int(value)) or (int(value) > int(max_val))):
        print('Wartosc musi byc nie mniejsza niz', min_val,
              'i nie wieksza niz', max_val, sep=' ', end='\n')
        value = input(text)

    return int(value)


def display_menu():
    menu_selection = 0
    print('\nMenu:')
    print('1 - Wyświetlanie listy studentów')
    print('2 - Edycja listy studentów')
    print('3 - Wyswietlanie wybranych studentów')
    print('4 - Odczytywanie listy z pliku')
    print('5 - Zapisywanie listy do pliku')
    print('6 - Koniec programu')

    print('\n')
    menu_selection = defense_int_input("Wybierz operacje: ", 1, 6)

    return menu_selection


def load():
    try:
        with open("bin.dat", "rb") as f:
            students_list = pickle.load(f)
            return students_list

    except Exception:
        pass


def edycja_menu():
    print("Co chcesz zrobic?")
    print("1. Dodac ucznia")
    print("2. Usunac ucznia")
    print("3. Modyfikacja ocen")

    odp = int(input())
    return odp


def edycja_wybor(wybor):
    if wybor == 1:

        dodawanie_ucznia()

    elif wybor == 2:

        usuwanie_ucznia()

    elif wybor == 3:

        modyfikacja_ocen()


def dodawanie_ucznia():
    print("Podaj imie:", end=' ')
    imie = input()
    print("Podaj nazwisko:", end=' ')
    nazwisko = input()
    print("Podaj index number:", end=' ')
    numer = input()

    oceny = []

    print("Ile ocen chcesz dodac?")
    x = int(input())
    for i in range(x):
        oceny.append(int(input(f"Podaj {i+1} ocene:")))

    nowy = Student(imie, nazwisko, numer, oceny)

    students_list.append(nowy)


def usuwanie_ucznia():
    print("twoja lista:")
    for student in students_list:
            student.show()
            print()
    print("Usunac jednego ucznia czy wiecej? [j/w]")
    x = input()

    if x == "j":
        print("podaj ktory element usunac:", end = " " )
        a = int(input())
        students_list.pop(a-1)
    elif x == "w":
        print("podaj zakres uczniow do usuniecia:")
        a = int(input("od ktorego:"))
        b = int(input("do ktorego:"))

        del students_list[a-1:b-1]

def modyfikacja_ocen():
    while 1:

        print("Oceny którego ucznia chcesz modyfikowac?")
        u = int(input())
        print ("Oceny ucznia:")
        students_list[u-1].show_rating()
        students_list[u-1].change_grades()
        
        print ("Czy chcesz kontynuować zmiany ocen? [t/n]")
        x = input()

        if x == "t":
            pass
        else:
            break


def wyswietlanie_menu():
	print("Na jakiej podstawie wybrac studentow?")
	print("1. Średnia ocen większa niż")
	print("2. Średnia ocen mniejsza niż")
	print("3. Numer z listy")

	wybor = int(input("Podaj opcje:"))
	return wybor


def wyswietlanie(wybor):
	if wybor == 1:
		w_srednia_g()

	elif wybor == 2:
		w_srednia_d()

	elif wybor == 3:
		w_numer()


def w_srednia_g():
	print("Podaj od jakiej sredniej w gore podac:")
	x = float(input())
	for student in students_list:
		if student.avg_rating() >= x:
			student.show()

def w_srednia_d():
	print("Podaj od jakiej sredniej w dol podac:")
	x = float(input())
	for student in students_list:
		if student.avg_rating() <= x:
			student.show()


def w_numer():
	print("Ilu studentow wyswietlic?")
	x = int(input())

	if x == 1:
		print("Podaj numer z listy:")
		a = int(input())
		print(students_list[a-1])
	elif x > 1:
		for i in range (x):
			students_list[int(input("Podaj numer:"))-1].show()


def save(students_list):
    with open("bin.dat", "wb") as f:
        pickle.dump(students_list, f)


print('Lista studentów.')
amount_of_students = 0
students_list = []

#student1 = Student("Rafał", "Nowak", 123456, [1, 2, 3, 4, 5])
#student2 = Student("Jan", "Kowalski", 234567, [2, 3, 4, 5])
#student3 = Student("Hanna", "Szymańska", 345678, [3, 4, 5])
#student4 = Student("Maja", "Jankowska", 456789, [4, 5])

#students_list.append(student1)
#students_list.append(student2)
#students_list.append(student3)
#students_list.append(student4)


#with open("bin.dat", "rb") as f:
#    s_l = pickle.load(f)
#    print(f"s_l: {s_l}")
#    for s in s_l:
#        s.show()

menu_selection = display_menu()


while(menu_selection < 6):

    if menu_selection == 1:
        print('\nLista studentów:\n')

        for student in students_list:
            student.show()
            print()


    elif menu_selection == 2:
        wybor = edycja_menu()
        edycja_wybor(wybor)

    elif menu_selection == 3:
        wybor = wyswietlanie_menu()
        wyswietlanie(wybor)

    elif menu_selection == 4:
        students_list = load()

    elif menu_selection == 5:
        save(students_list)
        print('Zapisano do pliku.')

    menu_selection = display_menu()