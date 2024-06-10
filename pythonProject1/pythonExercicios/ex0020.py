# Exercício 20 – Sorteando uma ordem na lista
""" O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. """
from random import  shuffle
nome1 = input('nome do primeiro aluno: ')
nome2 = input('nome do segundo aluno: ')
nome3 = input('nome do terceiro aluno: ')
nome4 = input('nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('a ordem apresentada será')
print(lista)
