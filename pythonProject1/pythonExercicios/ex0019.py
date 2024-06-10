# Exercício 19 – Sorteando um item na lista
""" Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
 lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""
# modo math
import random
nome1 = input('nome do primeiro aluno: ')
nome2 = input('nome do segundo aluno: ')
nome3 = input('nome do terceiro aluno: ')
nome4 = input('nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = [random.choice(lista)]
print('o aluno sorteado é {}'.format(escolhido))

# modulo from
from random import choice
nome1 = input('nome do primeiro aluno: ')
nome2 = input('nome do segundo aluno: ')
nome3 = input('nome do terceiro aluno: ')
nome4 = input('nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = [choice(lista)]
print('o aluno sorteado é {}'.format(escolhido))
