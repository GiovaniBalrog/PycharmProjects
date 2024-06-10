#  Exercício 50 – Soma dos pares
soma = 0
cont = 0
for c in range(1, 7):
   n = int(input('digite o {} valor: '.format(c)))
   if n % 2 ==0:
      soma += n
      cont += 1
print('voce informou: {} números PARES e a soma foi: {}'.format(cont, soma))


'''
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''