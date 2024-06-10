#Exercício 15 – Aluguel de Carros
#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
a = float(input('Quanntos dias alugados? '))
b = float(input('Quantos km rodado? '))
a = a * 60  # soma o aluguel do carro custa == R$60 por dia
b = b * 0.15  # soma cada km rodado é == R$0,15
total= a + b
#jeito guanabara mais simples == pago (a * 60)+(b * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))
