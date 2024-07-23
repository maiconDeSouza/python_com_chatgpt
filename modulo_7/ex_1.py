"""
- Crie dois conjuntos e aplique todas as operações básicas 
(união, interseção, diferença e diferença simétrica).
"""

import random


def gerar_numero():
    numero = random.randint(1, 50)
    return numero


conjunto_1 = set()
conjunto_2 = set()

while True:
    if len(conjunto_1) != 10:
        conjunto_1.add(gerar_numero())

    if len(conjunto_2) != 10:
        conjunto_2.add(gerar_numero())

    if len(conjunto_1) == 10 and len(conjunto_2) == 10:
        break


print("Conjunto 1 -> ", conjunto_1)
print("Conjunto 2 -> ", conjunto_2)

print("união ->", conjunto_1 | conjunto_2)
print("interseção", conjunto_1 & conjunto_2)
print("diferença", conjunto_1 - conjunto_2)
print("simétrica", conjunto_1 ^ conjunto_2)
