"""
**3. Classes Abstratas e Métodos Abstratos**
   - Crie uma classe abstrata `Forma` com um método abstrato `calcular_area`. Crie duas 
   subclasses `Quadrado` e `Triangulo` que implementam o método `calcular_area`.

"""

from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        raise NotADirectoryError("Tem que implementar")


class Quadadro(Forma):
    def calcular_area(self, x, y):
        return x * y


class Triangulo(Forma):
    def calcular_area(self, base, altura):
        return (base * altura) / 2


q_1 = Quadadro()
t_1 = Triangulo()

print(q_1.calcular_area(5, 5))
print(t_1.calcular_area(3, 3))
