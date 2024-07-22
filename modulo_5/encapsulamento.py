class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente!")

    def consultar_saldo(self):
        return self.__saldo


conta = ContaBancaria("Dante", 1000)
conta.depositar(500)
conta.sacar(200)
print(conta.consultar_saldo())  # Saída: 1300
