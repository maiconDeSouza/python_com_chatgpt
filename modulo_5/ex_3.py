"""
3. **Encapsulamento em Produto**
    - Crie uma classe `Produto` com atributos privados `nome` e `preco`. 
    Adicione métodos públicos para acessar e modificar esses atributos. Crie 
    um método para aplicar um desconto ao preço do produto.
"""


class Produto:
    def __init__(self, nome, preco) -> None:
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            raise ValueError("O preço deve ser maior ou igual a zero")

    def aplicar_desconto(self, percentual):
        if 0 <= percentual <= 100:
            desconto = (percentual / 100) * self.__preco
            self.__preco -= desconto
        else:
            raise ValueError("O percentual de desconto deve ser entre 0 e 100")


caneta = Produto("Caneta", 1.53)


print(caneta.nome)
caneta.nome = "Caneta Azul"
print(caneta.nome)

print(caneta.preco)
caneta.aplicar_desconto(10)
print(caneta.preco)
