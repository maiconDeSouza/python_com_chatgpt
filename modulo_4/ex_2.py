"""
2. **Classe Conta Bancária**
   - Crie uma classe `ContaBancaria` com os atributos `saldo` e 
   `titular`. Adicione métodos para depositar, sacar e consultar o saldo.
"""


class ContaBancaria:
    def __init__(self, titular, saldo_inicial) -> None:
        self.titular = titular
        self.saldo_inicial = saldo_inicial

    def depositar(self, valor):
        self.saldo_inicial += valor
        return "Deposito feito com sucesso!"

    def sacar(self, valor):
        if self.saldo_inicial < valor:
            return "Saldo insuficiente!"
        else:
            self.saldo_inicial -= valor
            return "Saque realizado com sucesso!"

    def consultar_saldo(self):
        return f"Olá {self.titular}, seu saldo é de {self.saldo_inicial}"


cliente_1 = ContaBancaria("Dante", 1000)
print(cliente_1.depositar(100))
print(cliente_1.sacar(1500))
print(cliente_1.sacar(200))
print(cliente_1.consultar_saldo())
