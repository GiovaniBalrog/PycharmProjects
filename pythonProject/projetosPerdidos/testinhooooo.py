'''import json
pessoa = {


class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def Correu(self, caminhou):
        if caminhou == "+":
            print("corre pra caramba")
        elif caminhou == "-":
            print(f' não correu hoje')



Pessoa = Pessoa('giovane', '28', 'masculino')
print(Pessoa.nome, Pessoa.idade, Pessoa.sexo)
Pessoa.Correu("+")

}
'''
'''
with.open('aula01.json', 'w') as arquivo:
    json.dump(pessoa,.arquivo)'''