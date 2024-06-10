#Exercício 10 – Conversor de Moedas
real = float(input('quanto dinheiro vc tem na carteira? R$'))
us = real / 5.03
euro = real / 5.56
B = real / 208.325
print('com R${:.2f} você pode comprar\n US${:.2f} \n euro$ {:.2f} \n bitcoin$ {:.2f}    '. format(real, us, euro, B))
