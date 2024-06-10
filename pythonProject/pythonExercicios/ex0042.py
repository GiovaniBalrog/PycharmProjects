#  Exercício 42 – Analisando Triângulos v2.0
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo! ', end='')
    if r1 == r2 == r3:
       print('EQUILÁTERO: todos os lados iguais ')
    elif r1 != r2 != r3 != r1:
       print('ESCALENO: todos os lados diferentes')
    else:
       print('ISÓSCELES: dois lados iguais, um diferente')
else:
    print('Os segmento acima não podem formar triângulo')

'''
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

'''