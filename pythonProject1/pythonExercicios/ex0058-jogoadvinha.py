#  Exercício 58 – Jogo da Adivinhação v2.0
from random import randint
computador = randint(0, 10)  # faz o computador "pensar"
print('sou seu computador... vou pensar em um numero entre 0 e 10. tente adivinhar ...')
print('você consegue adivinhar qua foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = str(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True

print('Acertou com {}  tentativas. PARABÉNS!!!'.format(palpites))

'''
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''