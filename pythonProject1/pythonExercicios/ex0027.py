# Exercício 27 – Primeiro e último nome de uma pessoa
n = str(input('digite seu nome completo: ')).strip()
nome = n.split()
print('muito prazer em te conhecer! ')
print('seu primeiro nome é: {} '.format(nome[0]))
print('seu segundo nome é: {} '.format(nome[len(nome)-1]))

'''
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente.
'''