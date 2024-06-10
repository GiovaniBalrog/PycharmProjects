#  Aula 13 – Estrutura de repetição for
''' ==> estrutura de reptiçao com variavel de controlem <== '''
'''
for c in range(0, 7, 2):  # ele nao considera o ultimo numero
    print(c)
print('fim')
'''


'''
n = int(input('digite um numero'))
for c in range(0, n+1):
    print(c)
print('fim')
'''
'''
i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
'''
'''
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('fim')
'''
'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('a soma total dos valores é igual: {}'.format(s))
'''
'''
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”,
 que é uma estrutura versátil e simples de entender. Por exemplo:

for c in range(0, 4):

print(c)

print(‘Acabou’)
'''

texto = 'python'
novaString = ''
for letra in texto:

    if letra == 't':
        continue  # pular para o próximo laço
        novaString += letra.upper()
    elif letra == 'h':
        novaString += letra.upper()

        break         # usado para o codigo terminar o laço
    else:
        novaString += letra
print(novaString)


