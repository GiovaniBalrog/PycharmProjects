#  Exercício 37 – Conversor de Bases Numéricas
numero = int(input('Digite Um Numero inteiro: '))
print('''escolha uma das opçoes a baixo
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal
''')
opção = int(input('sua opção: '))
if opção == 1:
    print('{} Convertido para binario é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
        print('{} Convertido para octal é igual a {}'.format(opção, oct(numero)[2:]))
elif opção == 3:
    print('{} Convertido para hexadecimal é igual a {}'.format(opção, hex(numero)[2:]))
else:
    print('opção invalida tente novamente')


'''
Exercício Python 37:
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal.
'''