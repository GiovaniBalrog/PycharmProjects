# def é uma rotina coisas que acontece constantemente o ideal é criar uma função
'''
# criando minha primeira função
def mostraLinha():
    print('\033[1:31m!==\033[1:34m' * 20)    # \033[1:31m enfeitando com cor


# no python a regra é antes do programa principal, sempre deixar duas linhas vazias.
mostraLinha()
print('giovani')
mostraLinha()
print('valdir')
mostraLinha()
print('lindines')
mostraLinha()
'''

'''
def contatos(cliente):  # parametro  # criando função linhas
    print('--' * 30)  # linhas para dividir o elemento
    print(cliente)  # testo
    print('--' * 30)    # linhas para dividir o elemento

# toda a ves que repetir a palavra contato a linha pe adicionada automaticamente
contatos('Giovani') # parametro
contatos('Valdir')  # parametro
contatos('Lindines')    # parametro

'''

'''  Definindo uma função
def primeiraFunc():
    print('Hello World')
primeiraFunc()
'''

''' Definindo uma função com parâmetro
def primeiraFunc(nome):
    print('Hello {}'.format(nome))
primeiraFunc('Aluno')
'''

'''
def funcLeitura():
    for i in range(0, 5):
        print("Número " + str(i))
funcLeitura()
'''

''' Função para somar números
def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
    print("Soma: ", firstnum + secondnum)
# Chamando a função e passando parâmetros
addNum(45, 3)
'''

''' Variável Global
var_global = 10  # Esta é uma variável global

def multiply(num1, num2):
    var_global = num1 * num2  # Esta é uma variável local
    print(var_global)
multiply(5, 25)
print(var_global)
'''

''' Variável Local
var_global = 10  # Esta é uma variável global
def multiply(num1, num2):
    var_local = num1 * num2   # Esta é uma variável local
    print(var_local)
multiply(5, 25)
print(var_local)
'''

''' Funções Built-in   # sao funções que ja existem dentro da biblioteca do python
abs()
abs()
bool()
bool()
************** isso é para lembrar que não preciso criar funçoes que ja existem
'''

'''
# Erro ao executar por causa da conversão
idade = int(input("Digite sua idade: "))
if idade > 13:
    print("Você pode acessar o Facebook")
int("26")

float("123.345")


str(14)


len([23,34,45,46])


array = ['a', 'b', 'c']

max(array)


min(array)
array = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']

max(array)


min(array)


list1 = [23, 23, 34, 45]

sum(list1)
'''

"""
#  Criando funções usando outras funções

import math

def numPrimo(num):
    '''
    Verificando se um número
    é primo.
    '''
    if (num % 2) == 0 and num > 2:
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"
print(numPrimo(541))
"""

"""  # Fazendo split dos dados
def split_string(text):
    return text.split(" ")
texto = "Esta função será bastante útil para separar grandes volumes de dados."
# Isso divide a string em uma lista.
print(split_string(texto))
['Esta', 'função', 'será', 'bastante', 'útil', 'para', 'separar', 'grandes', 'volumes', 'de', 'dados.']

# Podemos atribuir o output de uma função, para uma variável
token = split_string(texto)
print(token)
"""

'''
caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"
def lowercase(text):
    return text.lower()
lowercased_string = lowercase(caixa_baixa)
lowercased_string
'''

'''
def cliente(contato):
    print('===' * 30)
    print(contato)
    print('===' * 30)

c = 0
while c < 10:
    nome = str(input('Didite o nome do cliente: '))
    cliente(nome)
    print(nome)

'''

'''
def soma(a, b):
    s = a + b
    print(s)


soma(2, 3)
soma(3, 5)
soma(5, 8)
'''

'''
def contador(*num):
    print(num)


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
'''
''' dobrado os valores da minha lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''
'''

'''
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')
soma(5, 2)
soma(2, 9, 4)

