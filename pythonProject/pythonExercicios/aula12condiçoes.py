#  Aula 12 – Condições Aninhadas
nome = str(input('Qual é seu nome? ')).capitalize()
print('Seja Bem Vindo,{} seu nome esta amarzenado! '.format(nome))
if nome == 'Giovani':
    print('Que nome lindo! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
     print('seu nome é bem feminino')
elif nome in 'Ana cladia de jesus':
     print('que bonito nome vc tem')
else:
 print('nome normal qualquer')

'''(.capitalize()) sempre um ponto antes do codigo de atribuiçao
  vai pasar todas as caracteristicas e para minusculas com essecao da primeira letra que continuara MAIUSCULAS 
  '''

'''
Nessa aula, vamos aprender como criar estruturas condicionais aninhadas,
 usando os comandos if.. elif.. else em programas Python.
'''