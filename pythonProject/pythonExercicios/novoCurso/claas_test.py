# criando uma classe para clientes
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basico", "premium"]
        if plano in self.lista_planos:   # { if = se } { in = esta } dentro da lista_planos
            self.plano = plano
        else:
            raise Exception("plano invalido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("plano invalido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"ver filme {filme}")
        elif self.plano == "premium":
            print(f"ver filme {filme}")
        elif self.plano == "basico" and plano_filme == "premium":
            print("Faça um upgrade para ver esse filme")
        else:
            print("plano invalido")


Cliente = Cliente("gehh", "giovanegavioes@gmail.com", "basico")
print(Cliente.plano)
Cliente.ver_filme("Harry potter", "premium")

# no botao de upgrade
Cliente.mudar_plano("premium")
print(Cliente.plano)
Cliente.ver_filme("Harry potter", "premium")
