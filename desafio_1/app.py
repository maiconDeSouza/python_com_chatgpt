import os
import time


class Livro:
    @staticmethod
    def criar_livro(titulo, autor, ISBN):
        new_livro = {
            "Título": titulo,
            "Autor": autor,
            "ISBN": ISBN,
            "Disponível": True
        }
        return new_livro


class Usuario:
    @staticmethod
    def criar_usuarios(nome, id):
        new_usuario = {
            "ID": id,
            "Nome": nome,
            "Livros_emprestados": []
        }
        return new_usuario


class Biblioteca:
    def __init__(self) -> None:
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, titulo, autor, ISBN):
        new_livro = Livro.criar_livro(titulo, autor, ISBN)
        self.livros.append(new_livro)
        print(f'{new_livro["Título"]} por {new_livro["Autor"]} (ISBN: {
              new_livro["ISBN"]}) - cadastrado com sucesso!')

    def emprestar_livro(self, ISBN_livro, ID_usuario):
        for livro in self.livros:
            if livro["ISBN"] == ISBN_livro:
                if not livro["Disponível"]:
                    print("Livro não está disponível!")
                    return
                livro["Disponível"] = False
                for usuario in self.usuarios:
                    if usuario["ID"] == ID_usuario:
                        usuario["Livros_emprestados"].append(livro)
                        print("Livro emprestado com sucesso!")
                        return
                print("Usuário não encontrado")
                return
        print("Livro não encontrado!")

    def devolver_livro(self, ISBN_livro, ID_usuario):
        for usuario in self.usuarios:
            if usuario["ID"] == ID_usuario:
                for livro in usuario["Livros_emprestados"]:
                    if livro["ISBN"] == ISBN_livro:
                        livro["Disponível"] = True
                        usuario["Livros_emprestados"].remove(livro)
                        print("Livro devolvido com sucesso!")
                        return
                print("Livro não está emprestado para este usuário")
                return
        print("Usuário não encontrado")

    def adicionar_usuario(self, nome, id):
        new_usuario = Usuario.criar_usuarios(nome, id)
        self.usuarios.append(new_usuario)
        print(f'{new_usuario["ID"]} - {new_usuario["Nome"]
                                       } - cadastrado com sucesso!')

    def mostrar_livros_disponiveis(self):
        for livro in self.livros:
            if livro["Disponível"]:
                print(livro)

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)


def limpar_terminal(tempo=0):
    time.sleep(tempo)
    os.system("cls" if os.name == "nt" else "clear")


bi = Biblioteca()

menu = """
# 1 cadastrar novo livro;
# 2 cadastrar novo usuario;
# 3 emprestar um livro;
# 4 devolver um livro;
# 5 sair;
"""
while True:
    print(menu)
    op = input()

    if op == "1":
        limpar_terminal()
        print("Digite o título do livro:")
        titulo = input()
        print("Digite o autor:")
        autor = input()
        print("Digite o ISBN:")
        isbn = input()
        bi.adicionar_livro(titulo, autor, isbn)
        limpar_terminal(5)
    elif op == "2":
        limpar_terminal()
        print("Digite o nome do usuário:")
        nome = input()
        print("Digite o ID:")
        id_usuario = input()
        bi.adicionar_usuario(nome, id_usuario)
        limpar_terminal(5)
    elif op == "3":
        limpar_terminal()
        print("-----Livros Disponíveis-----")
        bi.mostrar_livros_disponiveis()
        print("-----Usuários-----")
        bi.mostrar_usuarios()
        print("----------")
        print("Digite o ISBN do livro:")
        isbn = input()
        print("Digite o ID do usuário:")
        id_usuario = input()
        bi.emprestar_livro(isbn, id_usuario)
        limpar_terminal(5)
    elif op == "4":
        limpar_terminal()
        print("Qual o ID do Usuário:")
        id_usuario = input()
        print("Qual o ISBN do livro que você está devolvendo:")
        isbn = input()
        bi.devolver_livro(isbn, id_usuario)
        limpar_terminal(5)
    elif op == "5":
        break
    else:
        print("Opção inválida!")
        limpar_terminal(2)
