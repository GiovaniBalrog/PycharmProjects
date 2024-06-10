#  Exercício 33 – Maior e menor
a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('tercriro valor: '))
# Verificar quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificar quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi o {}'.format(maior))

''' 
Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''