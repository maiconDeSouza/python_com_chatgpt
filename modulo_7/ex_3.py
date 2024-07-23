"""
**Exercício:**
- Implemente uma fila de tarefas usando deque e manipule as tarefas (adicionar, remover).
"""

from collections import deque
import os

tarefas = []

fila_de_tarefas = deque(tarefas)

menu = """
# 1 - cadastrar tarefa;
# 2 - tarefa concluida;
# 3 - visualizar tarefas;
# 4 - sair;
"""

while True:
    print(menu)
    op = input()
    os.system('cls')

    if op == '1':
        print("Digite sua tarefa")
        tarefa = input()
        fila_de_tarefas.append(tarefa)
    elif op == '2':
        tarefa_concluida = fila_de_tarefas.popleft()
        print(f"Tarefa {tarefa_concluida} com sucesso!")
    elif op == '3':
        print(fila_de_tarefas)
    elif op == '4':
        break
    else:
        print("Opção não")
