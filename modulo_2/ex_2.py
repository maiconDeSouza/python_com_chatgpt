"""
2. Crie uma lista com 10 números inteiros. Utilize slicing para exibir:
   - Os primeiros 5 números
   - Os últimos 5 números
   - Todos os números nas posições ímpares da lista
"""

lista = [x for x in range(1, 11)]

lista_5_primeiros = lista[0:5]
lista_5_ultimos = lista[5:10]
lista_par = [x for x in lista if x % 2 == 0]

print(lista)
print(lista_5_primeiros)
print(lista_5_ultimos)
print(lista_par)
