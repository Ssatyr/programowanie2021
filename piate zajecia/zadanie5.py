from funkcjaLiniowa import funkcjaLiniowa
from funkcjaKwadratowa import funkcjaKwadratowa
from zbiorFunkcji import zbiorFunkcji
from wykresFunkcji import wykresFunkcji
from Menu import display_menu,display_remove_function_menu_2, display_add_function_menu, display_remove_function_menu, return_new_float_value_or_previous_one, return_not_empty_new_string_or_previous_one

print('Program rysujacy wykresy funkcji')
zbior_funkcji = zbiorFunkcji()
wykresy_funkcji = wykresFunkcji(zbior_funkcji)
x_min = -10
x_max = 10
y_min = None
y_max = None
step = 0.0001
file_name = "data.dat"

while(True):
    menu_selection = display_menu()
    if menu_selection == 1:
        while(True):
            menu_add_function_selection = display_add_function_menu()
            if menu_add_function_selection == 1:

                a = float(input("Podaj wartosc parametru 'a': "))
                b = float(input("Podaj wartosc parametru 'b': "))
                funkcja = funkcjaLiniowa.create_function(a=a, b=b)
                zbior_funkcji.add_function(funkcja)

            elif menu_add_function_selection == 2:

                a = float(input("Podaj wartosc parametru 'a': "))
                b = float(input("Podaj wartosc parametru 'b': "))
                c = float(input("Podaj wartosc parametru 'c': "))
                funkcja = funkcjaKwadratowa.create_function(a=a, b=b, c=c)
                zbior_funkcji.add_function(funkcja)

            elif menu_add_function_selection == 3:
                break
            else:
                print("Niewlasciwy wybor. Wybierz dostepna opcje 1, 2 lub 3")

    elif menu_selection == 2:
        while(True):
            zbior_funkcji.show_function()
            remove_menu_selection = display_remove_function_menu()

            if remove_menu_selection == 1:

                index = int (input ("Podaj index: "))
                zbior_funkcji.delete_function_by(index-1)

            elif remove_menu_selection == 2:

                remove_menu_selection_2 = display_remove_function_menu_2()

                if remove_menu_selection_2 == 1:

                    a = float(input("Podaj wartosc parametru 'a': "))
                    b = float(input("Podaj wartosc parametru 'b': "))
                    funkcja = funkcjaLiniowa.create_function(a=a, b=b)
                    zbior_funkcji.delete_function(funkcja)

                elif remove_menu_selection_2 == 2:
                    a = float(input("Podaj wartosc parametru 'a': "))
                    b = float(input("Podaj wartosc parametru 'b': "))
                    c = float(input("Podaj wartosc parametru 'c': "))
                    funkcja = funkcjaKwadratowa.create_function(a=a, b=b, c=c)
                    zbior_funkcji.delete_function(funkcja)


            elif remove_menu_selection == 3:
                break

            else:
                print("Niewlasciwy wybor. Wybierz dostepna opcje 1, 2 lub 3")

    elif menu_selection == 3:
        wykresy_funkcji._show_plot()

    elif menu_selection == 4:
        x_min = return_new_float_value_or_previous_one("Podaj minimalna wartosc na osi x", x_min)
        x_max = return_new_float_value_or_previous_one("Podaj maksymalna wartosc na osi x", x_max)
        y_min = return_new_float_value_or_previous_one("Podaj minimalna wartosc na osi y", y_min)
        y_max = return_new_float_value_or_previous_one("Podaj maksymalna wartosc na osi y", y_max)
        wykresy_funkcji.set_x_range(x_min, x_max)
        wykresy_funkcji.set_y_range(y_min, y_max)
        step = return_new_float_value_or_previous_one("Podaj krok obliczen", step)
        wykresy_funkcji.set_step(step)

    elif menu_selection == 5:
        wykresy_funkcji.plot()

    elif menu_selection == 6:
        file_name = return_not_empty_new_string_or_previous_one("Podaj nazwe pliku", file_name)
        zbior_funkcji.save_to_file("data.dat")

    elif menu_selection == 7:
        file_name = return_not_empty_new_string_or_previous_one("Podaj nazwe pliku", file_name)
        zbior_funkcji.read_from_file("data.dat")

    else:
        break























