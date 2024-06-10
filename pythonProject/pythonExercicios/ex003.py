#Exercício 3 – Somando dois números
n1 = int(input('digite um numero:'))
n2 = int(input('digite mais um numero:'))
s = n1+n2
# print('a soma entre', (n1), 'e', (n2), 'é o que vale', format(s))
# código mais pratico atualizado
print('a soma entre {} e {} é o que vale {}'.format(n1, n2, s))