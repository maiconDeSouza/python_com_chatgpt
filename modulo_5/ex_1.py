"""
1. **Classe Veículo e Subclasses**
    
    - Crie uma classe `Veiculo` com um método `mover`. Crie subclasses `Carro` 
    e `Bicicleta` que sobrescrevem o método `mover` com comportamentos específicos.
"""


class Veiculo:
    rodas = 0

    def mover(self):
        raise NotImplementedError("Este método deve ser sobrescrito")

    def numero_de_rodas(self):
        return f"tem {self.rodas} rodas"


class Carro(Veiculo):
    rodas = 4

    def mover(self):
        return f"O carro deu partida e pode começar andar"

    def numero_de_rodas(self):
        return super().numero_de_rodas()


class Bicicleta(Veiculo):
    rodas = 2

    def mover(self):
        return f"O cliclista pedalou para a Bike andar"

    def numero_de_rodas(self):
        return super().numero_de_rodas()


carro_1 = Carro()
bike_1 = Bicicleta()

print(carro_1.mover())
print(carro_1.numero_de_rodas())

print(bike_1.mover())
print(bike_1.numero_de_rodas())
