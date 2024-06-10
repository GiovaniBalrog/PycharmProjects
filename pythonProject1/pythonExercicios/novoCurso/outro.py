# 'w+'  essa função serve para,  'w+' serve para zerar o e reescrever

'''  adiciona coisas no arquivo
'a+' essa função serve para, adiciona coisas no arquivo sem apagar nada dentro dele, ele tambem coloca o cursor no final do arquivo
'''

# 'r+' essa função serve para, 'r' serve para simplesmente só ler o conteudo do arquivo
#  essa função serve para
#  essa função serve para

'''  remover o arquivo por completo
import os
os.remove('abc.txt') #  para remover o arquivo por completo
'''




'''
file = open('abc.txt', 'w+')  # essa função serve para criar um arquivo
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')
file.write('linha 4\n')
file.write('linha 5\n')
file.write('linha 6\n')

file.seek(0, 0)      # essa função serve para chamar o cursor para posição inicial do arquivo
print('lendo linhas:')
print(file.read())        # essa função serve para ler tudo que tem no arquivo jogar ne uma string e exibir na tela
print('###############')

file.seek(0, 0)    # jogou o cursor de-novo para o começo do arquivo e leu linha por linha
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

file.seek(0, 0)   # jogou o cursor de-novo para o começo do arquivo
print(file.readlines())  # essa função serve para jogar linha por linha dentro de uma lista



file.close()

# 'w+' serve para zerar o e reescrever


'''
'''
# gerenciador de contexto

with open ('abc.txt', 'w+') as file:  #
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')

    file.seek(0)
    print(file.read())
    
  
'''

with open('abc.txt', 'w+') as file:  #
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')

    file.seek(0)
    print(file.read())


