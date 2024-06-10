#  Exercício 44 – Gerenciador de Pagamentos
print('{:=^40}'.format('lojas valdir'))
preço= float(input('preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO
[1] a vista dinheiro\cheque: 10% de desconto
[2] a vista cartão 5% 
[3] 2x no cartão: preço formal
[4] 3x ou mais no ''')
opçoes = int(input('Qual das opçoes? '))
if opçoes == 1:
    total = preço - (preço * 10 / 100)
    print('dinheiro ou cheque avista 10% de desconto')
elif opçoes == 2:
    total = preço - (preço * 5 / 100)
    print('avista no cartão 5% de desconto')
elif opçoes == 3:
    total = preço
    parcela = total / 2
    print('em ate 2x no cartão ')
    print('sua compra sera parcelada em 2x vezes de {:.2f}'.format(parcela))
elif opçoes == 4:
    total = preço + (preço * 20/100)
    totalpar = int(input('Qanta parcelas? '))
    parcela = total / totalpar
    print('3x ou mais no cartão: 20% de juros')
    print('sua compra sera parcelada em: {}x de R${:.2f}'.format(totalpar,parcela))
else:
    total = preço
    print('OPÇÃO INVALIDA TENTE NOVAMENTE')
print('sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))


'''
Exercício Python 44:
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
'''