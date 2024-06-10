#Exercício 12 – Calculando Descontos
q=float(input(' Qual é o preço do produto? R$  '))
r = q - ( q * 5 / 100)
print('o peroduto que custava {:.2f},\n na promoção com desconto de 5% \n vai custar {:.2f}'.format(q, r))
