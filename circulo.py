import math

class Circulo:
    radio = 0

    def __init__(self, id, radio):
        self.id = id
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
