"""
**4. Métodos Especiais**
   - Crie uma classe `Produto` com atributos `nome` e `preco`. Implemente os métodos especiais `__str__` 
   e `__repr__` para representar o objeto como uma string. Adicione também o método `__eq__` para comparar 
   dois produtos com base em seu nome e preço.
"""

from abc import ABC, abstractmethod


class Produtos(ABC):
    @abstractmethod
    def __init__(self, nome, marca, preco) -> None:
        self.nome = nome
        self.marca = marca
        self.preco = preco

    def __str__(self) -> str:
        return f"{self.nome} da marca {self.marca} com o preço {self.preco}"

    def __repr__(self) -> str:
        return f"nome = {self.nome}, marca = {self.marca}, preço = {self.preco}"

    def __eq__(self, other) -> bool:
        return self.nome == other.nome and self.marca == other.marca and self.preco == other.preco


class Caneta(Produtos):
    def __init__(self, nome, marca, preco) -> None:
        self.nome = nome
        self.marca = marca
        self.preco = preco


caneta_1 = Caneta("Caneta Azul", "Bic", 1.23)
caneta_2 = Caneta("Caneta Azul", "Bic", 1.23)
caneta_3 = Caneta("Caneta Azul", "Compac", 1.23)
print(caneta_1)
print(repr(caneta_1))
print(caneta_1 == caneta_2)
print(caneta_1 == caneta_3)
