def dobrar(x): return x * 2


print(dobrar(3))

lista = [1, 2, 3, 4]

lista_dobrada = list(map(lambda x: x * 2, lista))
print(lista_dobrada)

lista_de_pares = list(filter(lambda x: x % 2 == 0, lista))
print(lista_de_pares)
