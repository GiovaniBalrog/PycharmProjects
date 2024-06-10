#Aula 7 – Operadores Aritméticos
n1 = int(input('um valor:  '))
n2 = int(input('outro valor:  '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma vale {}, o produto é {} e a divisão é {:.3f} '.format(s, m, d), end='>>>')
print('Divisão Inteira {} e Potência {}'.format(di, e))
# \n significa nova linha para quebrar
# end='' significa mesma linha para nao quebrar
# {:.3f} 3 => significa a quantidade casa decimais, f =>significa ponto frutuante
