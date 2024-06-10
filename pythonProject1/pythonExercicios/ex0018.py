# Exercício 18 – Seno, Cosseno e Tangente
""" Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
 cosseno e tangente desse ângulo."""
# modulo math
"""import math
ângulo = float(input('Digite o ângulo que vc deseja: '))
seno = math.sin(math.radians(ângulo))
print('o ângulo de {} tem o seno de: {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('o ângulo de {} tem o cosseno de: {:.2f} '.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem o tangente de: {:.2f}'.format(ângulo, tangente))
"""
# modulo from
from math import radians, sin, cos, tan
ângulo: float = float(input('Digite o ângulo que vc deseja: '))
seno = sin(radians(ângulo))
print('o ângulo de {} tem o seno de: {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('o ângulo de {} tem o cosseno de: {:.2f} '.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem o tangente de: {:.2f}'.format(ângulo, tangente))
