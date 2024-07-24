from uuid import uuid4


class Funcionario:
    def __init__(self, nome, cargo, salario) -> None:
        self.id = self.gerar_uuid()
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def gerar_uuid(self):
        return str(uuid4())

    def atualizar_cargo(self, novo_cargo):
        self.cargo = novo_cargo

    def atualizar_salario(self, novo_salario):
        self.salario = novo_salario

    def __str__(self):
        return f'ID: {self.id}, Nome: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario}'


class Empresa:
    def __init__(self) -> None:
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, id):
        self.funcionarios = [
            funcionario for funcionario in self.funcionarios if funcionario["id"] != id]

    def atualizar_funcionario(self, id, novo_cargo=None, novo_salario=None):
        for funcionario in self.funcionarios:
            if funcionario["id"] == id:
                if novo_cargo:
                    funcionario
