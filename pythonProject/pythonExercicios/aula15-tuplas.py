'''
lanche = ('hamburger', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'eu vou comer {comida}')
print('comi pra caramba! ')
'''
'''
lanche = ('hamburger', 'suco', 'pizza', 'pudim')
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos} ')
print('comi pra caramba! ')
'''
'''
lanche = ('hamburger', 'suco', 'pizza', 'pudim', 'batata frita')
for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')
print('comi pra caramba! ')
'''
'''
lanche = ('hamburger', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'eu vou comer {comida}')
print('comi pra caramba! ')
'''
'''concatenar a + b = c'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
''' a ordem influencia 
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
'''

#   Tupla
'''  tupla não tem uma limitação, ela é um objeto proprio para garantir
a integridade dos dados, mais se eu quiser alterar um elemento eu tenho algumas alternativas
'''
''' conversão de uma trupa para uma lista para a alteração de elementos 
t2 = ('A', 'B', 'C')
print(t2)
list_t2 = list(t2)   # para a conversão de tupa para lista
list_t2.append('D')  # metodo .append() serve para adicionar um item a lista
t2 = tuple(list_t2)  #  conversão de lista para tupa
print(t2)            # imprimir a tela
'''
