class Carro:
    rodas = 4

    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo


meu_carro = Carro("Chevrolet", "Celta")

print(meu_carro.modelo)
print(meu_carro.rodas)
print(Carro.rodas)
