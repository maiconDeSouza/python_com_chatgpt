"""
5. Crie dois conjuntos com alguns elementos em comum. Exiba a união, interseção e diferença entre esses conjuntos.
"""

conjunto_a = {15, 14, 1, 23, 12}
conjunto_b = {1, 2, 15}

new_conjunto = conjunto_a.union(conjunto_b)
print(new_conjunto)

intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)

diferenca = conjunto_a.difference(conjunto_b)
print(diferenca)
