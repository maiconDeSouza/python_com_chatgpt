risco = "-" * 10
lista_vazia = []
lista_com_valores = [1, 2, 3]
lista_com_construtor = list("oi")
lista_com_construtor_2 = list(range(4, 7))

print(lista_vazia)
print(lista_com_valores)
print(lista_com_construtor)
print(lista_com_construtor_2)

print(f"{risco}Teste com copia!{risco}")
copia_1 = lista_com_valores
copia_2 = list(lista_com_valores)
lista_com_valores.append("a")
print("lista_com_valores ->", lista_com_valores, "id ->", id(lista_com_valores))
print("copia_1 ->", copia_1, "id ->", id(copia_1))
print("copia_2 ->", copia_2, "id ->", id(copia_2))
print(f"{risco}lista_mista{risco}")
lista_mista = [1, "dois", 3.0, [4, 5]]
print(lista_mista)

print(f"{risco}usando insert para adicionar uma valor na lista_mista na posição de indice 2{risco}")
lista_mista.insert(2, "Casa")
print(lista_mista)
