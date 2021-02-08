from Funkcja import Funkcja
import pickle

class zbiorFunkcji:
    def __init__(self):
        self.set_of_functions = []

    def add_function(self, function: Funkcja):
        self.set_of_functions.append(function)

    def delete_function(self, function: Funkcja):
        self.set_of_functions.remove(function)

    def delete_function_by(self, index: int):
        if(self.set_of_functions[index]):
            del self.set_of_functions[index]

    def save_to_file(self, file_name):
        with open(file_name, "wb") as f:
            pickle.dump(self.set_of_functions, f)

    def read_from_file(self, file_name):
        try:
            with open(file_name, "rb") as f:
                self.set_of_functions = pickle.load(f)
        except Exception:
            pass

    def show_function(self):
        i = 0
        for f in self.set_of_functions:
            i+=1
            print("Index: ", i)
            print(f.show())

