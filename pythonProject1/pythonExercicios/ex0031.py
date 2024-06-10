#  Exercício 31 – Custo da Viagem
distância = float(input('Qual a distancia da sua viagem? '))
print('Voce esta prestes a começar uma viagem de {}km'.format(distância) )
''' if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45 '''
preço = distância * 0.50 if distância <= 200 else distância * 0.45  # if simplificada
print('E o preço da su passagem sera de R${:.2f}'.format(preço))

'''
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
 cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
 '''