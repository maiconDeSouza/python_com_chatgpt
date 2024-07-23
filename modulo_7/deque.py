from collections import deque

lista = [15, 23, 4, 8, 9]

fila = deque(lista)
print(fila)
fila.append(11)
print(fila)
fila.popleft()
print(fila)
