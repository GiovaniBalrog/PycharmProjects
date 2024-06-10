# Exercício 22 – Analisador de Textos
from django.template.defaultfilters import upper, lower
n = str(input('digite seu nome completo? ')).strip()  # strip ==> é uma string cortada elimina os espaços antes e depois do texto
print('analisando seu nome...')
print('nome completo em maiúsculas: {} '.format(upper(n)))
print('nome completo em minúsculas: {} '.format(lower(n)))
print('Seu nome tem ao todo: {} letras '.format(len(n) - n.count(' ')))  # elimina os espaços do meio do texto
#print('Seu primeiro nome tem : {} letras'.format(n.find(' ')))
'''comando maior mais mais sinples de intender '''
separa = n.split()
print('Seu primeiro nome é {} e ele tem {} letra'.format(separa[0], len(separa[0])))

'''' Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome. '''