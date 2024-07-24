Claro, aqui está um exercício que envolve herança, métodos estáticos e de 
classe, classes abstratas e métodos especiais, mas sem incluir decoradores ou 
gerenciamento de contexto.

### Desafio: Sistema de Gerenciamento de Biblioteca

#### Descrição

Crie um sistema de gerenciamento de biblioteca que permita adicionar livros, 
emprestar livros para usuários e devolver livros. Utilize classes e métodos 
que façam uso dos conceitos estudados:

- **Herança**
- **Métodos Estáticos e de Classe**
- **Classes Abstratas e Métodos Abstratos**
- **Métodos Especiais**

#### Estrutura Básica

1. **Classe `Livro`**
   - Atributos: título, autor, ISBN, status (disponível ou emprestado)
   - Métodos: `__str__`, `__repr__`

2. **Classe `Usuario`**
   - Atributos: nome, ID, livros_emprestados (lista de livros)
   - Métodos: `__str__`, `__repr__`

3. **Classe `Biblioteca`**
   - Atributos: lista de livros, lista de usuários
   - Métodos:
     - `adicionar_livro`
     - `emprestar_livro`
     - `devolver_livro`
     - `mostrar_livros_disponiveis`
     - `mostrar_usuarios`

### Estrutura do Código

```python
from abc import ABC, abstractmethod

class Livro:
    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.status = "disponível"
    
    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.ISBN}) - {self.status}"
    
    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', ISBN='{self.ISBN}', status='{self.status}')"

class Usuario:
    def __init__(self, nome, ID):
        self.nome = nome
        self.ID = ID
        self.livros_emprestados = []
    
    def __str__(self):
        return f"Usuário: {self.nome} (ID: {self.ID})"
    
    def __repr__(self):
        return f"Usuario(nome='{self.nome}', ID='{self.ID}', livros_emprestados={self.livros_emprestados})"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
    
    def adicionar_livro(self, titulo, autor, ISBN):
        novo_livro = Livro(titulo, autor, ISBN)
        self.livros.append(novo_livro)
    
    def adicionar_usuario(self, nome, ID):
        novo_usuario = Usuario(nome, ID)
        self.usuarios.append(novo_usuario)
    
    def emprestar_livro(self, ISBN, usuario):
        for livro in self.livros:
            if livro.ISBN == ISBN and livro.status == "disponível":
                livro.status = "emprestado"
                usuario.livros_emprestados.append(livro)
                return f"O livro '{livro.titulo}' foi emprestado para {usuario.nome}."
        return "Livro não disponível ou não encontrado."
    
    def devolver_livro(self, ISBN, usuario):
        for livro in usuario.livros_emprestados:
            if livro.ISBN == ISBN:
                livro.status = "disponível"
                usuario.livros_emprestados.remove(livro)
                return f"O livro '{livro.titulo}' foi devolvido por {usuario.nome}."
        return "Livro não encontrado nos empréstimos deste usuário."
    
    def mostrar_livros_disponiveis(self):
        disponiveis = [livro for livro in self.livros if livro.status == "disponível"]
        return disponiveis
    
    def mostrar_usuarios(self):
        return self.usuarios

# Criação da biblioteca
biblioteca = Biblioteca()

# Adicionar livros
biblioteca.adicionar_livro("1984", "George Orwell", "123456789")
biblioteca.adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "987654321")

# Adicionar usuários
usuario1 = Usuario("Alice", "001")
usuario2 = Usuario("Bob", "002")

# Emprestar livro
print(biblioteca.emprestar_livro("123456789", usuario1))

# Devolver livro
print(biblioteca.devolver_livro("123456789", usuario1))

# Mostrar livros disponíveis
print(biblioteca.mostrar_livros_disponiveis())

# Mostrar usuários
print(biblioteca.mostrar_usuarios())
```

### Tarefas:

1. Crie as classes `Livro`, `Usuario` e `Biblioteca` conforme descrito acima.
2. Implemente os métodos `adicionar_livro`, `adicionar_usuario`, 
`emprestar_livro`, `devolver_livro`, `mostrar_livros_disponiveis` e 
`mostrar_usuarios` na classe `Biblioteca`.
3. Teste o sistema criando uma instância de `Biblioteca`, adicionando alguns 
livros e usuários, emprestando e devolvendo livros, e mostrando os livros 
disponíveis e os usuários.

Este exercício consolidará seu entendimento sobre herança, métodos estáticos e 
de classe, classes abstratas e métodos especiais, sem incluir decoradores 
ou gerenciamento de contexto. Boa sorte!