class Cachorro:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def latir(self):
        return f"{self.nome} está latindo!"


cachorro_1 = Cachorro("Dante", 3)

print(cachorro_1.nome)
print(cachorro_1.latir())
