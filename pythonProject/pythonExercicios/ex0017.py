# Exercício 17 – Catetos e Hipotenusa
''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
 Calcule e mostre o comprimento da hipotenusa. '''
''''
from math import trunc
co = float(input('Comprimento do cateto oposto:  '))
ca = float(input('Comprimento do cateto adjecente:  '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(' Comprimento do cateto oposto: {} \nComprimento do cateto adjecente: {} \nA hipotenusa vai medir: {:.2f} '. format(co, ca, hi))
'''
from math import hypot
co = float(input('Comprimento do cateto oposto:  '))
ca = float(input('Comprimento do cateto adjecente:  '))
hi = hypot(co, ca)
print('A hipotenusa vai medir{:.2f}'.format(hi))