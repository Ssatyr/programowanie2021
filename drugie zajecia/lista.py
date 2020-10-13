import random
from statistics import median


def menu():
	print("Menu:")
	print("1. Generowanie listy")
	print("2. Sortowanie listy")
	print("3. Wyswietlanie liczb")
	print("4. Usuwanie liczb")
	print("5. Dodawanie liczb")
	print("6. Średnia itd")
	print("7. Koniec programu")

def generowanie_listy(lista):
	print ("ile elementow ma miec lista?")
	elementy = int(input())

	print ("Czy maja być wygenerowane losowo?  [t/n]")
	losowosc = input()

	if losowosc.lower() == "t":
		for i in range (elementy) :
			lista.append(random.randint(0,100))
	elif losowosc.lower() == "n":
		for i in range (elementy) :
			lista.append(int(input(f"Wprowadź {i+1} element: ")))



def usuwanie_liczb(lista):
	print(f"twoja lista: \n {lista}")
	print("Usunac element czy zakres? [e/z]")
	x = input()

	if x == "e":
		print("podaj ktory element usunac:", end = " " )
		a = int(input())
		lista.pop(a-1)
	elif x == "z":
		print("podaj zakres elementow do usuniecia:")
		a = int(input("od ktorego:"))
		b = int(input("do ktorego:"))

		del lista[a-1:b-1]


def dodawanie_liczb(lista):
	print(f"twoja lista: \n {lista}")
	print("Dodac jeden element czy wiecej? [j/w]")
	x = input()

	if x == "j":
		print("podaj jaki element chcesz dodac:", end = " " )
		a = int(input())
		lista.append(a)
	elif x == "w":
		print("ile elementow dodad?")
		a = int(input())
		for i in range (a) :
			lista.append(int(input(f"Wprowadź {i+1} element: ")))


print ("Witaj!")
print ("Wybierz co chcesz zrobić:")
menu()

lista_m = []

odpowiedz = int(input())

while odpowiedz != 7:

	if odpowiedz == 1:
		generowanie_listy(lista_m)

	elif odpowiedz == 2:
		lista_m.sort()

	elif odpowiedz == 3:
		print ("lista:")
		print (lista_m)

	elif odpowiedz == 4:
		usuwanie_liczb(lista_m)

	elif odpowiedz == 5:
		dodawanie_liczb(lista_m)

	elif odpowiedz == 6:
		print ("Wyswietlanie sumy sredniej itd:")
		print (f"srednia: {sum(lista_m)/len(lista_m)}")
		print (f"max: {max(lista_m)}")
		print (f"min: {min(lista_m)}")
		print (f"suma: {sum(lista_m)}")
		print (f"liczba elementow: {len(lista_m)}")
		print (f"mediana: {median(lista_m)}")
		print (f"posortowane: {sorted(lista_m)}")

	else:
		print ("podaj inny numer")

	menu()
	print("Co chcesz zrobić?")
	odpowiedz = int(input())