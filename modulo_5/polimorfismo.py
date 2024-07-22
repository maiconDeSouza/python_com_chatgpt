class Forma:
    def area(self):
        raise NotImplementedError(
            "Este método deve ser sobrescrito pelas subclasses")


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        import math
        return math.pi * (self.raio ** 2)


formas = [Retangulo(5, 3), Circulo(7)]

for forma in formas:
    print(forma.area())
