dicionario_vazio = {}  # Dicionário vazio
# Dicionário com chaves e valores
dicionario_com_valores = {"nome": "Maria", "idade": 25}

print(dicionario_vazio)
print(dicionario_com_valores)

print("Add -> end no dicionario com valores")
dicionario_com_valores["end"] = "Rua de lá, 23"
print(dicionario_com_valores)

print("Removemento o end usando o pop")
end = dicionario_com_valores.pop("end")
print(dicionario_com_valores)
print("retorno salvo na variavel end ->", end)

chaves = dicionario_com_valores.keys()  # Obtém todas as chaves
valores = dicionario_com_valores.values()  # Obtém todos os valores
itens = dicionario_com_valores.items()  # Obtém todos os pares chave-valor

print("chaves ->", chaves)
print("valores ->", valores)
print("itens ->", itens)
