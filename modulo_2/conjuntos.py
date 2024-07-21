conjunto_vazio = set()  # Conjunto vazio
conjunto_com_valores = {1, 2, 3, 4, 5}  # Conjunto de inteiros

print(conjunto_vazio)
print(conjunto_com_valores)

print("**Adicionando Itens com add**")
conjunto_com_valores.add(6)  # Adiciona 6 ao conjunto
print(conjunto_com_valores)

print("**Removendo 3 com remove. O discard não emite erro quando não é encontrado o valor**")
conjunto_com_valores.remove(3)
print(conjunto_com_valores)

print("**Operações com Conjuntos**")
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
uniao = conjunto_a.union(conjunto_b)  # União: {1, 2, 3, 4, 5}
interseccao = conjunto_a.intersection(conjunto_b)  # Interseção: {3}
diferenca = conjunto_a.difference(conjunto_b)  # Diferença: {1, 2}

print("union ->", uniao)
print("ntersection ->", interseccao)
print("difference ->", diferenca)
