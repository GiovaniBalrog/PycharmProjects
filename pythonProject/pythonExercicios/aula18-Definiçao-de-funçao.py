# def ==> definição de função, (Função é uma rotina coisas que acontece constantemente.)
#  def é usada para criar funções que ainda nao existem dentro do meu repertorio.

'''
# Definindo uma função
def primeiraFunc():
    print('Hello World')
primeiraFunc()
'''

'''
# Definindo uma função com parâmetro
def primeiraFunc(nome):
    print(f'Hello {nome}')
primeiraFunc('giovane')
primeiraFunc('lind')
'''

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
contatos('ana')
contatos('nataly')
'''

'''
def soma(a, b):
    s = a + b
    print(s)

# programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)
'''

'''
# passando dois parametros na soma 
def soma(a, b):
    print(f'A = {a} B = {b}')
    s = a + b
    print(f'A Soma A + B = {s}')


# programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)
'''

'''
def contador(* num):
        tam = len(num)
        print(f'Recebi Os Valores {num} E São Ao Todo {tam} números')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(5, 6, 9, 7, 8)
'''

'''
# dobrado os valores da minha lista
def dobra(lst):
    pos = 0  # variavel (pos) que começa na posição 0
    while pos < len(lst):   # em quanto a (pos)==> posição for menor que o tamanho da lista
        lst[pos] *= 2   # a lista na posição atual receba o dobro dela *= 2
        pos += 1    # pos é igual a pos mais um


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)  # parametro valores = lst
print(valores)
'''


'''
# desempacotamento
def soma(* valores):
    s = 0   # soma recebe 0
    for num in valores: # para cada numeros em valores
        s += num    # soma mais = num
    print(f'Somando Os Valore {valores} temos {s}')


# programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)
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
def aument_percentual (valor, percentual):
    return valor + (valor * percentual / 100)


ap = aument_percentual(5, 10)
print(ap)
ap = aument_percentual(100, 10)
print(ap)
ap = aument_percentual(10, 10)
print(ap)
ap = aument_percentual(15, 100)
print(ap)
'''


