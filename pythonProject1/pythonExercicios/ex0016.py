# Exercício 16 – Quebrando um número
# primera forma
'''import math
num = float(input('Diga um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {} '. format(num, math.floor(num)))'''
# segunda forma
'''from math import trunc
num = float(input('Diga um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {} '. format(num, trunc(num)))'''
# terceiro modo
num = float(input('Diga um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {} '. format(num, int(num)))
