#  Exercício 35 – Analisando Triângulo v1.0
print('-='*20)
print('Analizador de triangulos')
print('-='*20)
r1 = int(input('primeiro segmento: '))
r2 = int(input('segundo segmento: '))
r3 = int(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar triangulo! ')
else:
    print('\033[0:33:41mOs segmentos acima nao podem formar triangulo!')
# sistema de cores ===> \033[0:33:41m

'''
Exercício Python 35:
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''