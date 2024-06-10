class Pessoa:


# OopCompanion:suppressRename
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.nome} diz: Olá, mundo!")
        print(f"{self.nome} diz: Bora Começar o dia ")

# Criando um objeto da classe Pessoa
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
pessoa1 = Pessoa(nome, idade)

# Chamando o método falar do objeto pessoa1
pessoa1.falar()
