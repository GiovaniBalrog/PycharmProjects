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
