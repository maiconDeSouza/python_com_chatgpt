from uuid import uuid4


class Funcionario:

    @staticmethod
    def gerar_uuid(self):
        return str(uuid4())

    # def gerar_novo_funcionario(self):


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
