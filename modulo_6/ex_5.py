"""
**5. Gerenciamento de Contexto**
   - Crie uma classe `ConexaoBanco` que simula a abertura e o fechamento de uma conexão com um banco de dados. 
   Implemente os métodos `__enter__` e `__exit__` para garantir que a conexão seja 
   fechada adequadamente.
"""


class ConexaoBanco:
    def __init__(self, url_banco):
        self.url_banco = url_banco
        self.conexao = None

    def __enter__(self):
        print("Abrindo conexão com o banco de dados:", self.url_banco)
        self.conexao = self._conectar()
        return self.conexao

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conexao:
            print("Fechando conexão com o banco de dados:", self.url_banco)
            self._desconectar(self.conexao)
            self.conexao = None
        if exc_type:
            print("Erro:", exc_type, exc_val, exc_tb)

    def _conectar(self):
        return "Conexão simulada com sucesso!"

    def _desconectar(self, conexao):
        print("Conexão simulada fechada com sucesso!")


with ConexaoBanco("banco_exemplo.com") as conexao:
    print("Executando consulta SQL na conexão:", conexao)
