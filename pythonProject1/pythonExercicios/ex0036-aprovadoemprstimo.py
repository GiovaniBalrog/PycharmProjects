#  Exercício 36 – Aprovando Empréstimo
casa = float(input('valor da casa: R$'))
salario = float(input('Salariodo comprador: R$'))
ano = int(input('Quantos anos de financiamento: '))
prestação = casa / (ano * 12)
minimo = salario * 30 / 100
if salario <= minimo:
    print('Parabens vc foi aprovado')
elif salario >= minimo:
    print('Sinto muito! \033[0:33:41mEmprestimo Negados!\033[0:33:41m')
print('para pagar uma casa de R${:.2f} em  {} '.format(casa,ano), end='')
print('a prestação será de R${:.2f}'.format(prestação))

'''
Exercício Python 36:
 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.
'''