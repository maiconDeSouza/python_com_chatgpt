# Gerador simples
def gerador():
    yield 1
    yield 2
    yield 3


for valor in gerador():
    print(valor)
