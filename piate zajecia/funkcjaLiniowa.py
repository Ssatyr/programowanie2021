import numpy as np
from Funkcja import Funkcja

class funkcjaLiniowa(Funkcja):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = []
        self.y = []
        self.step = 0.0001
        self.x_min = -10
        self.x_max = 10
        self.type = "liniowa"
        self.info = f"f(x) = {self.a}*x + {self.b}"

    def set_x_range(self, x_min, x_max):
        self.x_min = x_min
        self.x_max = x_max

    def set_step(self, step):
        self.step = step

    def calculate(self):
        self.x.clear()  
        self.y.clear()
        self.x = list(np.arange(self.x_min, self.x_max, self.step))
        self.y = [self.a*x+self.b for x in self.x]  

    @classmethod
    def create_function(cls, **kwargs):
        if kwargs['a']:
            a = int(kwargs['a'])
            b = int(kwargs['b'])
            return funkcjaLiniowa(a, b)
        else:
            raise Exception
            ("Nalezy podac parametry a i b funkcji liniowej")
