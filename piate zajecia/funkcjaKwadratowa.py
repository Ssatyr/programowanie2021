import numpy as np
from Funkcja import Funkcja

class funkcjaKwadratowa(Funkcja):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.x = []
        self.y = []
        self.step = 0.0001
        self.x_min = -10
        self.x_max = 10
        self.type = "kwadratowa"
        self.info = f"f(x) = {self.a}*x**2 + {self.b}*x + {self.c}"

    def set_x_range(self, x_min, x_max):
        self.x_min = x_min
        self.x_max = x_max

    def set_step(self, step):
        self.step = step

    def calculate(self):
        self.x.clear()  
        self.y.clear()
        self.x = list(np.arange(self.x_min, self.x_max, self.step))
        self.y = [self.a*x**2+self.b*x+self.c for x in self.x]

    def show(self):
        print("a: ", self.a)
        print("b: ", self.b)
        print("c: ", self.c)

    @classmethod
    def create_function(cls, **kwargs):
        if kwargs['a']:
            a = int(kwargs['a'])
            b = int(kwargs['b'])
            c = int(kwargs['c'])
            return funkcjaKwadratowa(a, b, c)
        else:
            raise Exception
            ("Nalezy podac parametry a, b i c funkcji kwadratowej")
