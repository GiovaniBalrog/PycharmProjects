'''
valores = ["leite", "café", "açúcar", "bolacha"]
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('cheguei ao final da lista')
'''

'''
list = [32, 53, 85, 10, 15, 17, 19]
soma = 0
for i in list:
    duble = i * 2
    soma += duble
print(f'A soma de todos os valores é: {soma}')
'''

'''
# com esse comando eu consigo dizer quantos itens tem na minha lista
list = [5, 6, 10, 13, 17]
cont = 0  # com esse comando eu consigo dizer quantos itens tem na minha lista
for i in list:
    cont += 1
print(cont)
'''

'''
# com esse comando eu consigo dizer quantos itens tem na minha lista

list = [5, 6, 10, 13, 17],['café', 'arroz', 'batata'], [1.200, 789, 'gehh', 'lind']
cont = 0  # com esse comando eu consigo dizer quantos itens tem na minha lista
for i in list[0]:  # código para saber quantos elementos tem no primeiro bloco
    cont += 1    # com esse comando eu consigo dizer quantos itens tem na minha lista
print(cont)  # com esse comando eu consigo dizer quantos itens tem na minha lista

'''

'''
#  pesquisa em lista
list = [5, 6, 7, 10, 50]
# loop através da lista
for item in list:  # se detro de lista tiver 5 repta numero encontrado
    if item == 5:
        print('numero encontrado')
'''

'''
#  esse código revela a chave
dic = {'ki':'giovani','k2':'da','k3':'silva'}
for item in dic:
    print(item)
'''

''''
#  esse código revela o resultado da chave e valor
dic = {'ki': 'Giovani', 'k2': 'Lindinês', 'k3': 'Valdir'}
for k,v in dic.items():
    print(k,v)
'''

'''
#  esse código revela o resultado do valor
dic = {'ki': 'Giovani', 'k2': 'Lindinês', 'k3': 'Valdir'}
for k, v in dic.items():  # k==> chave, v==> valor
    print(v)

'''

'''
# tambem posso alinhar uma lista dentro da outra
# criar uma lista de listas
list = [[1, 2, 3],[10, 15, 14], [10.1, 8.7, 2.3]]
a = list[0]   #  atribuindo um item da lista a uma variavel
print(a)

'''

'''
# esse código sort() serve para colocar a lista em ordem
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
print(valores)
'''

'''
#   segue a baixo alguns tipos de manipulação de lista  ==>
""" .append() para adicionar elementos a lista """
""" .insert(0, 'valores ')  para adicionar elementos a lista na posição desejada """
""" valores.sort(reverse=True) #   código serve para colocar alista em ordem reversa  """
"""  len(valores)   #  código serve para ver o comprimento ou a quantidade de elemento dentro da lista """
""" valores.sort() #  código para organizar,em ordem os elementos da lista """
'''

""" retornando chave e valor 
valores = []
valores.append(7)
valores.append(6)
valores.append(5)
valores.append(4)
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}! ')
print('cheguei ao final da lista!!!')
"""

""" ler valor pelo teclado e colocar dentro da lista
valores = list()
for cont in range(0, 6):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}! ')
print('cheguei ao final da lista!!!')
"""

"""
#  para criar uma cópia de uma lista sem fazer ligação
a = [2, 3, 4, 7]
# b = a  ''' assim liga uma na outra '''
b = a[:]   # ''' assim cria uma copia  todos os elementos de a copia para b   '''
b[2]=8  # alterar o elemento 2 na posição b para valor 8
print(f'Lista A{a}')
print(f'Lista B:{b}')
"""

"""
#   criar listas atraves de range
valores =list(range(1, 11))
print(len(valores))
"""

""""
lanche = ['dogão', 'hamburger', 'suco', 'pizza', 'sorvete',  'broa']
#   formas de deletar um elemento dentro de lista
lanche.pop(2)   # pela chave
lanche.remove('pizza')   # pelo elemento ou conteudo
del lanche[3]    # pela chave
if 'sorvete' in lanche:     # se tiver sorvete em lanche remova
    lanche.remove('sorvete')
print(lanche)
"""
# listas alinhadas
'''pessoas = [['lindy', 27], ['valdir', 4], ['Giovani', 28]]
print(pessoas[0][0])'''

'''
# copia de dados 
test = list()   # atribuindo uma lista na variavel teste
test.append('Giovani')  # atribuindo elementos a lista
test.append(28)  # atribuindo elementos a lista
novaList = list()  # criando nova lista
novaList.append(test[:])  # esse é o elemento utilizado para a [:] copia do dado 
test[0] = 'Valdir'
test[1] = 4
novaList.append(test[:])
print(novaList)
'''

'''
galera = [['maria', 50], ['nataly', 25], ['lindines', 28]]
for p in galera: # para cada [p] pessoa em [galera]
    print(f'{p[0]} tem {p[1]} anos de idade')
'''

'''
nome = list()
idade = list()
for c in range(0, 3):
    idade.append(str(input('Digite seu Nome: ')))
    idade.append(int(input('Digite Sua idade: ')))
    nome.append(idade[:])
    idade.clear()
    for p in nome:
        print(f'{p[0]}tem {p[1]} anos de idade')
print('--FIM--')
'''

'''
nome = list()
idade = list()
totmai = totmen = 0
for c in range(0, 3):
    idade.append(str(input('Digite seu Nome: ')))
    idade.append(int(input('Digite Sua idade: ')))
    nome.append(idade[:])
    idade.clear()
for p in nome:
    if p[1] >= 21:   # se idade maior igual 21
        print(f'{p[0]} de: {p[1]} anos. é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} de {p[1]} anos. menor de idade')
        totmen += 1
print(f'temos {totmai} maior e {totmen} menor de idade')
'''

''' a função enumerate() numera a string   '''




