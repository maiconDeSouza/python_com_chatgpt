from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        raise NotImplementedError("Precisa ser implementado na subclasse")

    @abstractmethod
    def andar(self):
        return "Andando..."


class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"

    def andar(self):
        return super().andar()


class Gato(Animal):
    def emitir_som(self):
        return "Miau"

    def andar(self):
        return super().emitir_som()


rex = Cachorro()
mioto = Gato()

print(rex.andar())
print(mioto.emitir_som())
