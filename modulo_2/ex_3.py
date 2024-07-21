"""
3. Crie uma tupla com 4 elementos. Acesse o segundo e o último elemento, e exiba-os. Crie uma nova tupla 
que adicione um quinto elemento à tupla original.
"""

tupla = tuple("CASA")
print(tupla)
print(tupla[1])
print(tupla[-1])
new_tupla = tupla + tuple("S")

print(new_tupla)
