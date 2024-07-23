"""
**1. Herança Múltipla**
   - Crie uma classe `Animal` com o método `falar`. Crie duas subclasses, `Cachorro` e `Gato`, 
   que sobrescrevem o método `falar` com sons específicos. Depois, crie uma classe `AnimalDeEstimacao` 
   que herda de ambas as classes `Cachorro` e `Gato`, e sobrescreve o método `falar` 
   para indicar que é um animal de estimação.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def falar(self):
        raise NotImplementedError("Implementar na subclass")


class Cachorro(Animal):
    def falar(self):
        return "Au au"


class Gato(Animal):
    def falar(self):
        return "Miau"


class AnimalDeEstimacao(Cachorro, Gato):
    def falar(self):
        return "Estimação"


dante = AnimalDeEstimacao

print(dante.falar())
