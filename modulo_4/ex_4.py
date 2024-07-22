"""
4. **Classe Livro**
   - Crie uma classe `Livro` com os atributos `titulo`, `autor` e `ano`. 
   Adicione um método para exibir informações sobre o livro.
"""


class Livro:
    def __init__(self, titulo, autor, ano) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def info(self):
        return f"O {self.titulo} tem o autor {self.autor} e foi lançado no ano de {self.ano}"


livro = Livro("O Hobbit", "J.R.R. Tolkien", 1937)
print(livro.info())
