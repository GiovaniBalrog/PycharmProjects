#  anotações das aulas
''' revisao
disciplina = input('digite uma disciplina:')
nota = float(input('digite uma nota: '))
semestre = int(input('digite um semestre de ((1 a 4)):'))
if disciplina == 'Geografia' and nota >= 50 and int(semestre) != 1:
    print('voce foi aprovado em %s com media final %r' % (disciplina, nota))
    print('voce foi aprovado em {} com media final {}'.format(disciplina, nota))
else:
    print('lamento, voce foi reprovando!!!')

'''
# estrutura de repetição for
'''para cada i ==> Siguinificado ==> item do meu conjunto de itens me retorna o comando dentro de
print('imprima na tela') 
for i in range(1, 11):
    print('{}° item'.format(i))
'''
'''list = ['leite', 'café', 'açucar']
for i in list:
    print('{}'.format(i))'''
'''estrutura for
tp = (2, 3, 4)
for c in tp:
    print(c)
'''
'''
list = ["leite", "café", "açúcar", "bolacha"]
for c in list:
    print(c)
'''
'''for c in range(0, 5):
    print('c')
'''
'''se o item # ==> (((num)) dividido por 2 for igual a 0 %, indica que é um numero par
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # conjunto de itens
for num in list:  # ==> itens
    if num % 2 == 0:  # divisão por dois e resto da divisão
        print(num)
'''
'''se cada caracteres  da minha sequencia de caracteres eu imprimo caracteres na tela
string é na verdade uma sequencia de caracteres
caracter = 'giovani da silva'
for c in caracter:
    print(c)
'''
'''
for i in range(0, 5):
    for a in range(0, 5):
        print('{}° item'.format(a))
'''
'''
list = [32, 53, 85, 10, 15, 17, 19]
soma = 0
for i in list:
    duble = i * 2
    soma += duble
print(soma)
'''
'''
list = [5, 6, 10, 13, 17]
cont = 0  # com esse comando eu consigo dizer quantos itens tem na minha lista
for i in list:
    cont += 1
print(cont)
'''
'''
list = [5, 6, 10, 13, 17],['café', 'arroz','batata'],[1.200, 789, 'gehh']
cont = 0  # com esse comando eu consigo dizer quantos itens tem na minha lista
for i in list[0]:  # código para saber quantos elementos tem no primeiro bloco
    cont += 1
print(cont)'''
#  pesquisa em lista
'''
list = [5, 6, 7, 10, 50]
# loop através da lista
for item in list:  # se detro de lista tiver 5 repta numero encontrado
    if item == 5:
        print('numero encontrado')
'''
'''esse código revela a chave
dic = {'ki':'giovani','k2':'da','k3':'silva'}
for item in dic:
    print(item)
'''
'''esse código revela o resultado da chave e valor
dic = {'ki': 'Giovani', 'k2': 'Da', 'k3': 'Silva'}
for k,v in dic.items():
    print(k,v)
'''
'''esse código revela o resultado do valor
dic = {'ki': 'Giovani', 'k2': 'Da', 'k3': 'Silva'}
for k, v in dic.items():  # k==> chave, v==> valor
    print(v)
'''
