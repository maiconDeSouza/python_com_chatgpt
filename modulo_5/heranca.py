class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        raise NotImplementedError("Este método deve ser sobrescrito")


class Cachorro(Animal):
    def emitir_som(self):
        return f"{self.nome} faz auau!"


class Gato(Animal):
    def emitir_som(self):
        return f"{self.nome} faz miau!"


class Elefante(Animal):
    def andar(self):
        return "Andando"


dog = Cachorro("Dante")
cat = Gato("Mioto")
elephant = Elefante("Dumbo")

print(dog.emitir_som())
print(cat.emitir_som())
print(elephant.emitir_som())
