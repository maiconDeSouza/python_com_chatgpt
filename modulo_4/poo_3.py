class Retangulo:
    def __init__(self, largura, altura) -> None:
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


meu_retangulo = Retangulo(5, 3)
print(meu_retangulo.area())
