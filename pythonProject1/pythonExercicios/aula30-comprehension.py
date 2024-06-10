# list comprehension
# comprensao de conjuntos em python
'''
numero = '012345678901234567890123456789012345678901234567890123456789'
n = 10
novo_numero = [numero[i:i + n] for i in range(0, len(numero), n)]
retorno = '.'.join(novo_numero)
print(numero)
print(novo_numero)
'''

carinho = []
carinho.append(('produto 1', 30))   # estou desempacotando a cada linha desse produto estou pegando o indice 0 e o indice 1
carinho.append(('produto 2', 20))
carinho.append(('produto 3', 50))


total = [(x, y) for x, y in carinho] # list comprehension

print(carinho)
print(total)







