#  Operador ternario em Python

'''
loogged_user = False

if loogged_user:
    msg = 'usuario logado.'
else:
    msg = 'usuario precisa logar.'

print(msg)

'''

#  Operador ternario em Python

'''   
# simplificando

loogged_user = False

msg = 'usuario logado.' if loogged_user else 'usuario precisa logar.'

print(msg)

'''


'''
idade = input('qual é sua idade? ')

if not idade.isnumeric():
    print('voce deve digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'pode acessar' if e_de_maior else 'não pode acessar'

    print(msg)

'''


#  =====================================  #

#   Expressão condicional com operador OR

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'luis'

variavel = a or b or c or d or e or g or f
print(variavel)

