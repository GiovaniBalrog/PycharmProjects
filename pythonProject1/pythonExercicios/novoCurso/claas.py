# orientacao a objeto

'''  caracteristica:
    - cor

    - altura

    - profundidade

    - largura
'''

class ControleRemoto:   # isso é um objeto: porque primeiro cria o objeto e as classes para depois utilizar as classes
    def __init__(self, cor, altura, profundidade, largura):  # isso é um objeto: porque primeiro cria o objeto e as classes para depois utilizar as classes
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade

    '''  metodos e funçoes:

    - passar de canal
    
    - mexer no volume
    
    - abrir a netflix
    
    - desligar
    
    '''
    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o volume")
        elif botao == "-":
            print("Diminue o volume")



conto_remoto = ControleRemoto("preto", "10cm", "5cm", "2cm") # caracteristica definida
print(conto_remoto.cor, 'esse é o controle 1') # caracteristica
conto_remoto.passar_canal("+") # função

conto_remoto2 = ControleRemoto("ciza", "10cm", "2cm", "2cm") # caracterica definida
print(conto_remoto2.cor, 'esse é controle 2') # caracteristica
conto_remoto2.passar_canal("-") #função
