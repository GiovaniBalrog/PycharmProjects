#  Exercício 38 – Comparando números

num1 = int(input('Diga um numero: '))
num2 = int(input('Dida outro numero: '))
if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
    print('o primeiro valor é maior')
elif num2 > num1:
    print('{} é maior que {}'.format(num2, num1))
    print('o segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')

'''elif num1 == num2: #####meu geito de fazer tudo ok
    print('Não existe maior, os dois são iguais') ###'''


'''
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''