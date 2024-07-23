class Matematica:
    @staticmethod
    def soma(a, b):
        return a + b

    @classmethod
    def descricao(cls):
        return f"Esta é a classe {cls.__name__}"


print(Matematica.soma(2, 3))
print(Matematica.descricao())
