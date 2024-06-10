#  Exercício 41 – Classificando Atletas
from datetime import date
atual = date.today().year
nasc = int(input('digite seu ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM'.format(idade))
if idade <= 14:
    print('Classificação: INFANTIL'.format(idade))
elif idade <= 19:
    print('Classificação: JÚNIOR'.format(idade))
elif idade <= 25:
    print('Classificação: SÊNIOR'.format(idade))
else:
    print('Classificação: MASTER'.format(idade))

'''
Exercício Python 041: 
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''