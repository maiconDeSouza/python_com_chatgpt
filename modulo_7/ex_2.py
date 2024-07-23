"""
- Crie um dicionário de estudantes e suas notas. Adicione, 
remova e modifique as entradas.
"""

alunos = {"Ana": [9.5, 8.7, 7.9], "João": [
    8.2, 9.1, 7.3], "Maria": [9.8, 9.4, 9.6]}
alunos["Pedro"] = [7.5, 8.2, 9.0]
del alunos["João"]
alunos["Ana"][1] = 8.9
print(alunos)
