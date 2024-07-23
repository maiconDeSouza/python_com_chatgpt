import os
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

uniao = conjunto1 | conjunto2
intersecao = conjunto1 & conjunto2
diferenca = conjunto1 - conjunto2

print(f"conjunto1 ->", conjunto1)
print(f"conjunto2 ->", conjunto2)

print(uniao)
print(intersecao)
print(diferenca)

conjunto3 = set()

while True:
    if len(conjunto3) == 10:
        break

    print("Digite um número:")
    numero = int(input())
    conjunto3.add(numero)
    os.system("cls")
    print(conjunto3)
