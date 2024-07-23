class GerenciadorArquivo:
    def __enter__(self):
        self.arquivo = open('exemplo.txt', 'w')
        return self.arquivo

    def __exit__(self, exc_type, exc_value, traceback):
        self.arquivo.close()


with GerenciadorArquivo() as f:
    f.write("Olá, mundo!")

# O arquivo é automaticamente fechado ao sair do bloco `with`
