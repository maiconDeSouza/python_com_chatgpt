class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return f"Seu nome é {self.nome}, sua idade é {self.idade}"

    def __repr__(self) -> str:
        return f"nome = {self.nome}, idade = {self.idade}"

    def __eq__(self, other) -> bool:
        return self.nome == other.nome and self.idade == other.idade


p_1 = Pessoa("Alice", 30)
p_2 = Pessoa("Alice", 30)
p_3 = Pessoa("João", 30)

print(p_1)
print(repr(p_1))
print(p_1 == p_2)
print(p_1 == p_3)
