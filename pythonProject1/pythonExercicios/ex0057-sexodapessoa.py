# Exercício 57 – Validação de Dados
sexo = str(input('informe seu sexo [M/F]:  ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. por favor, informe seu sexo: '.format(sexo))).upper().strip()[0]
print('sexo {} resgitrado com sucesso!'.format(sexo))

'''
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''