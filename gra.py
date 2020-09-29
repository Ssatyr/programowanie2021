import random

print ("Witaj w tej grze ja wylosuje liczbe z przedzialu 1-100 a ty musisz zgadnac jaka to! POWODZENIA!")

wylosowana = random.randint(1, 100)

podana = int(input("Podaj liczbe: "))

while podana != wylosowana:
	if podana > wylosowana:
		print ("za duzo")
	elif podana < wylosowana:
		print("za malo")

	podana = int(input("Podaj liczbe: "))

print ("Wygrales")