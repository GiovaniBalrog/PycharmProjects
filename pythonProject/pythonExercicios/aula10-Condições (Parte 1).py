#  Aula 10 – Condições (Parte 1)
'''
nome = str(input('Qual é seu nome? ')).upper()
if nome == 'GIOVANI':  #  condição simples
    print('que nome lindo vc tem!')
else:  #  condição compostas
    print('seu nome é uma merda')
print('bom dia, {}!'.format(nome))
'''
'''forma simplificada'''
n1 = float(input('Primeira nota do aluno '))
n2 = float(input('segunda nota do aluno '))
m = (n1 + n2) / 2
print('A sua media foi {:.1f}'.format(m))
print('Parabéns'if m >=6 else'estude mais!')



'''
Nessa aula, vamos aprender como utilizar estruturas condicionais
simples e compostas nos seus programas em Python.
 '''
