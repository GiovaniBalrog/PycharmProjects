from datetime import date
nome = 'giovani'
idade = 28
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)
atual = date.today().year
nacimento = atual - idade
print(f'{nacimento}\n nome:{nome} \n {idade} anos de idade\n {peso}kg \n imc:{imc:.2f} ')



