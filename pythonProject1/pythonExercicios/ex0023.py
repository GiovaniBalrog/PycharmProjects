# Exercício 23 – Separando dígitos de um número
num = int(input('digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o numero {}'.format(num))
print('unidade:{}'.format([u]))
print('dezena: {}'.format([d]))
print('centena: {}'.format([c]))
print('milhar: {} '.format([m]))

''' Exercício Python 23:
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''
