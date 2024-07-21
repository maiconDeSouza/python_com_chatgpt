"""
1. Crie uma lista com 5 números inteiros. Adicione um número no final, remova o segundo item e modifique o 
último item para um novo valor. Exiba a lista final.
"""

lista = list(range(1, 6))
print(lista)
lista.append(6)

lista.pop(1)
print(lista)

lista[-1] = "casa"
print(lista)
