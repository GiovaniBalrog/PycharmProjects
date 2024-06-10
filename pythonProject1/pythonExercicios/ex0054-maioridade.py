#  Exercício 54 – Grupo da Maioridade
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('em que ano {}º pessoa nasceu:'.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maior de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menor de idade'.format(totmenor))

'''
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''