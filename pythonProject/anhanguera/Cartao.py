# Definindo a classe base para os cartões
class CartaoBase:
    pass  # Esta classe pode conter métodos e atributos comuns a todos os tipos de cartão

# Definindo a classe para o cartão Gold, que herda da classe CartaoBase
class CartaoGold(CartaoBase):
    # Método para calcular o cashback para o cartão Gold
    def calcular_cash_back(self, valor):
        # Multiplica o valor da compra por 0.3 (30%) para calcular o cashback
        return valor * 0.3

# Definindo a classe para o cartão Platinum, que também herda de CartaoBase
class CartaoPlatinum(CartaoBase):
    # Método para calcular o cashback para o cartão Platinum
    def calcular_cash_back(self, valor):
        # Multiplica o valor da compra por 0.5 (50%) para calcular o cashback
        return valor * 0.5

# Criando uma instância do cartão Gold e calculando o cashback para uma compra de R$ 100
cartao_gold = CartaoGold()
cash_back_gold = cartao_gold.calcular_cash_back(100)

# Criando uma instância do cartão Platinum e calculando o cashback para uma compra de R$ 100
cartao_platinum = CartaoPlatinum()
cash_back_platinum = cartao_platinum.calcular_cash_back(100)

# Exibindo os resultados dos cálculos de cashback para ambos os cartões
print(f"Cashback para Cartão Gold: R${cash_back_gold:.2f}")
print(f"Cashback para Cartão Platinum: R${cash_back_platinum:.2f}")