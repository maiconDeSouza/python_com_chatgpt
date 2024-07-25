from uuid import uuid4
import os
import time


class Funcionario:

    @staticmethod
    def gerar_novo_funcionario(nome, cargo, salario):
        novo_funcionario = {
            "id": str(uuid4()),
            "nome": nome,
            "cargo": cargo,
            "salario": salario
        }
        return novo_funcionario


class Empresa:
    def __init__(self) -> None:
        self.funcionarios = []

    def adicionar_funcionario(self, nome, cargo, salario):
        novo_funcionario = Funcionario.gerar_novo_funcionario(
            nome, cargo, salario)
        self.funcionarios.append(novo_funcionario)
        print(f"{novo_funcionario["nome"]} -> {novo_funcionario["id"]}")

    def remover_funcionario(self, id):
        self.funcionarios = [
            funcionario for funcionario in self.funcionarios if funcionario["id"] != id]
        print("Excluido com sucesso!")

    def atualizar_funcionario(self, id, *, novo_cargo=None, novo_salario=None):
        for funcionario in self.funcionarios:
            if funcionario["id"] == id:
                if novo_cargo:
                    funcionario["cargo"] = novo_cargo
                if novo_salario:
                    funcionario["salario"] = novo_salario
        print("Funcionário editado!")

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)


def limpar_terminal(tempo=0):
    time.sleep(tempo)
    os.system("cls" if os.name == "nt" else "clear")


nova_empresa = Empresa()

menu = """
# 1 Cadastrar Funcionário,
# 2 Remover Funcionarío,
# 3 Editar Funcionário,
# 4 Listar Funcionários,
# 5 Sair.
"""

while True:
    print(menu)
    op = input()

    if op == "1":
        print("Digite o nome do novo funcionário:")
        nome = input()
        print("Digite o Cargo:")
        cargo = input()
        print("Digite o Sálario:")
        salario = input()
        nova_empresa.adicionar_funcionario(nome, cargo, salario)
        limpar_terminal(3)
    elif op == "2":
        nova_empresa.listar_funcionarios()
        print("Digite o ID do funcionário que deve ser excluído")
        id = input()
        nova_empresa.remover_funcionario(id)
        limpar_terminal(3)
    elif op == "3":
        nova_empresa.listar_funcionarios()
        print("Digite o Id do Funcionário que você quer editar")
        id = input()
        print("Quer editar o cargo? se sim digite o cargo ou não para manter:")
        cargo = input()
        print("Quer editar o salário? se sim digite o sálario ou não para manter:")
        salario = input()

        if cargo == "não" and salario == "não":
            print("Nada a fazer!")
        elif cargo != "não" and salario == "não":
            nova_empresa.atualizar_funcionario(id, novo_cargo=cargo)
        elif cargo == "não" and salario != "não":
            nova_empresa.atualizar_funcionario(id, novo_salario=salario)
        elif cargo != "não" and salario != "não":
            nova_empresa.atualizar_funcionario(
                id, novo_cargo=cargo, novo_salario=salario)
        else:
            print("Nada a fazer!")

        limpar_terminal(3)

    elif op == "4":
        nova_empresa.listar_funcionarios()
    elif op == "5":
        break
