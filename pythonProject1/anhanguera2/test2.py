'''
lista = [7, 4]
if lista[0] > lista[1]:
    aux = lista[1]
    lista[1]= lista[0]
    lista[0] = aux
print(lista)
'''


lista = [5, -1]
if lista[0] > lista[1]:
    lista[0], lista[1] = lista[1], lista[0]
print(lista)
