class Carteira:
    saldo = 0

    def adicionar_fundos(self, valor):
        self.saldo += valor
        print("Operação realizado com sucesso!")

    def remover_fundos(self, valor):
            if self.saldo >= valor:
                self.saldo -= valor
                print("operação concluidao!")
            else:
                print("Operação nao realizada. saldo insuficiente")
