"""
1. **Classe Pessoa**
   - Crie uma classe `Pessoa` com os atributos `nome` e `idade`. Adicione 
   um método para exibir uma saudação com o nome da pessoa.
"""


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self, saudacao="Olá"):
        return f"{saudacao}, {self.nome}!"


p_1 = Pessoa("Monique", 30)
print(p_1.saudacao("Bom dia"))
print(p_1.saudacao())
