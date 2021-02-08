from zbiorFunkcji import zbiorFunkcji


def defense_int_input(text, min_val, max_val):
    value = input(text)
    while ((int(min_val) > int(value)) or (int(value) > int(max_val))):
        print('Wartosc musi byc nie mniejsza niz', min_val, 
            'i nie wieksza niz', max_val, sep=' ', end='\n')
        value = input(text)
    return int(value)

def display_menu():
        print('\nMenu')
        print('1 - dodanie funkcji')
        print('2 - usuniecie funkcji')
        print('3 - wyswietlenie funkcji')
        print('4 - definiowanie parametrow wykresu funkcji')
        print('5 - generowanie wykresu funkcji')
        print('6 - zapisanie zbioru funkcji do pliku')
        print('7 - odczytanie zbioru funkcji do pliku')
        print('8 - koniec programu\n')

        menu_selection = defense_int_input('Wybierz operacje:', 1, 8)
        return menu_selection

def display_add_function_menu():
        print('\n1 - dodanie funkcji liniowej')
        print('2 - dodanie funkcji kwadratowej')
        print('3 - powrot do menu glownego\n')

        menu_selection = defense_int_input('Wybierz operacje:', 1, 3)
        return menu_selection


def display_remove_function_menu():

    print('1 - Usuniecie wedlug indeksu')
    print('2 - Usuniecie podanej funkcji')
    print('3 - powrot do menu glownego\n')

    menu_selection = defense_int_input('Wybierz operacje:', 1, 3)
    return menu_selection


def display_remove_function_menu_2():

    print('1 - Usuniecie f liniowej')
    print('2 - Usuniecie f kwadratowej')

    menu_selection = defense_int_input('Wybierz operacje:', 1, 2)
    return menu_selection


def return_new_float_value_or_previous_one(info: str, previous_value: float) -> float:
        try:
            value = float(input(f"{info} [{previous_value}]: "))
        except:
            value = previous_value
        return value

def return_not_empty_new_string_or_previous_one(info: str, previous_one: str) -> str:
        string = input(f"{info} [{previous_one}]: ")
        if string:
            return string
        else:
            return previous_one

