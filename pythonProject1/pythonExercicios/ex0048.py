#  Exercício 48 – Soma ímpares múltiplos de três
soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 ==0:
       cont = cont + 1  # um contador soma 1
       soma = soma + n  # um acumulador soma um valor
'''
        soma +=con
        cont += 1
        
'''

print('a soma total dos {} valores é : {}'.format(cont, soma))

'''
Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
'''