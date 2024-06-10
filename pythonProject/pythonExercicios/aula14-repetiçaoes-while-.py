#  Aula 14 – Estrutura de repetição while
'''
Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python.
Por exemplo:

c=1 while c !=10:

print(c)

c+=1

print(‘Acabou’)
'''
''' aula dois laços:
estrudoravde repetiçao com teste logico
o comando enquanto ==>> em ingles  ===>> 

(while)==> mais usado quando não sabe o limite
(for)==> mais usado quando vc sabe o limite

'''
'''c = 1
for c in range(10):
    print(c)
print('FIM')
'''
'''
c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')
'''
'''for c in range(1, 5):
    n = int(input('digite um valor: '))
print('FIM')'''
'''n = 1
while n != 0:
    n = int(input('digite um valor: '))
print('FIM')
'''
'''
r = 'S'
while r == 'S':
    n = int(input('digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM')
'''
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par +=1
        else:
            impar += 1
print('voce digitou {} numeros par e {} numeros impar'.format(par, impar))
'''

# estrutura de reptação loop while ==> significa, enquanto
'''
x = 0
while x < 10:
    print('\033[1:34m O valor de x  nessa interação é: ',x)
    print('x é ainda menor que 10, somando 1 a x')
    x += 1
else:
    print('\033[1:31m loop concluído !!!')
'''

''' Usando um loop para imprimir de 0 a 9
c = 0
while c < 10:  #  (((( 0 < 9 )))) enquanto o contador for menor que 0 imprima o valor da variável
    print(c)
    c += 1  # esse código serve para que algum momento a condição deixe de ser verdadeira
'''

'''enquanto a condição for verdadeira me retorna um valor repetidas vezes 
 **** importante acrescentar uma condição falsa, para que a verdadeira não caia ne um loop infinito
e trave o sistema operacional da maquina
 '''
''' comando break para freiar a interação
c = 0
while c < 100:  # enquanto o contador for menor que 0 imprima o valor da variável
    if c == 7:  # se contador chegar a 6 execute o o próximo comando ==> print ==> break
        print('\033[1:31mTUDO CERTO ATÉ AK!!!')
        break  # parar complement o programa quando encontrar
    else:
        pass
    print('\033[1:34m{}'.format(c))
    c += 1
'''
''' 
# COR print('\033[1:31m') 
'''
''' comando continue para pular uma interação
for verificador in 'Python':
    if verificador == 'h':
        continue
    print(verificador)
'''
'''
for i in range(2, 30):
    j = 2
    c = 0
    while j < i:
        if i % j == 0:
            c = 1
            j += 1
        else:
            j += 1
    if c == 0:
        print(str(i) + " ==> é um numero primo")
        c = 0
    else:
        c = 0
'''
n = s = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    s += n
#  print('A Soma vale {}'.format(s))
print(f'Somando todos os valores o resultado final é ==  {s}')

#   print(f'{}') ""f strings"" ==> essa é a nova atualização para saida formatada.
#   isso é uma tecnica chamada interpulção dentro de strings

