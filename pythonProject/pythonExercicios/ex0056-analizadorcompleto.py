#  Exercício 56 – Analisador completo
somaidade = 0  #  ela começa com 0 e recebe o resultado la em baixo
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('----- {}° ----- PESSOA '.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()
    somaidade += idade  #  a soma da idade recebe ela mesmo +  idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('o Homen mais velho é: {}e tem {} anos'.format(nomevelho, maioridadehomem))
print('Ao todo tem {} mulheres com menos de 20 anos '.format(totmulher20))

'''
para calcular a media de idade do grupo devo somar todas as idades e depois dividir pelo numero de pessoas
usando somaidade 
'''
'''
Exercício Python 56 : Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
 e quantas mulheres têm menos de 20 anos.
'''