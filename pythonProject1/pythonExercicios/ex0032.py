#  Exercício 32 – Ano Bissexto
from datetime import date

ano = int(input('Que ano quer analisar? digite o para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('O ano {} é bissexto'.format(ano))
else:
  print('O ano {} Não é bissexto'.format(ano))

'''
Exercício Python 32: Faça um programa
 que leia um ano qualquer e mostre se ele é bissexto
 '''