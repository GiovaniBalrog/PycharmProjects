#  Exercício Python 29 Radar Electronico
'''' so o (if) sem o else é estrutura de condiçao sinples '''
velocidade = float(input('Qual a velocidade atual do veiculo? '))
print('a velocidade atual é de {}km/h\n Tenha UM Excelente Dia!\n dirija com segurança  '.format(velocidade))
if velocidade > 80:
    print('MULTADO! vc ultrapassou o limite de velocidade permitido que é  de {}Km/h '.format(velocidade))
    multa = (velocidade-80) * 7
    print('Voce deve pagar a multa de R${:.2f}'.format(multa))
    print('a velocidade atual é de {}km/h\n Tenha um bom Dia!\n dirija com segurança  '.format(velocidade))


'''
Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.

'''