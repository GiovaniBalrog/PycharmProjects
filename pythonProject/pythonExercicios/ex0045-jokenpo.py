 #  Exercício 45 – GAME: Pedra Papel e Tesoura
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opçoes
[0] pedra
[1] papel
[2]tesoura
''')
jogador = int(input('Escolha sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO!!!')
sleep(3)
print('-=' * 12)
print('o computador jogou: {} '.format(itens[computador]))
print('jogador jogou: {} '.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 1: print('jogador venceu')
    elif jogador == 2: print('computador venceu')
    elif jogador == 0: print('empate venceu')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0: print('computador venceu')
    elif jogador == 1: print('empate')
    elif jogador == 2: print('jogador venceu')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0: print('jogador venceu')
    elif jogador == 1: print('computador venceu')
    elif jogador == 2: print('empate')
    else:
        print('JOGADA INVALIDA')

'''
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
'''