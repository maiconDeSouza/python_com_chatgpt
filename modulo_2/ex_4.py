"""
4. Crie um dicionário para armazenar informações de uma pessoa (nome, idade, cidade). Adicione um novo 
campo 'profissão', modifique a idade e remova o campo 'cidade'. Exiba o dicionário final.
"""

pessoa = {
    "nome": "Dante",
    "idade": 3,
    "cidade": "Santo André"
}

pessoa["Profissão"] = "Cão de Guarda"

pessoa["idade"] = 4

pessoa.pop("cidade")

print(pessoa)
