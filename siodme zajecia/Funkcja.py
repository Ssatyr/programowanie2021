from abc import ABC

class Funkcja(ABC):
    @classmethod
    def create_function(cls,  **kwargs):
        raise Exception("Cos poszlo nie tak")
