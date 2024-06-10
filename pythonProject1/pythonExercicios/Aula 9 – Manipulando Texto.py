# Aula 9 – Manipulando Texto
""" Nessa aula, vamos aprender operações com String no Python.
 As principais operações que vamos aprender são o Fatiamento de String,
 Análise com len(), count(), find(), transformações com replace(), upper(),
  lower(), capitalize(), title(), strip(), junção com join(). """
# formas de fatiamento
frase = 'Curso em video Python'
''' print(frase[9:13])  # hand ==> o último valor nao entra na contagem '''
print(frase[9:14])  # se quiser utilizar o, treze a chamada tem que ser ate o, catorze

# fatiar de doi em dois
""" print(frase[9:21:2])  # ==> ele vai pular de dois em dois res == vdopto """
""" print(frase[:5])  # ==> antes de doi pontos é onde vai começar depois de dois pontos é aonde ele vai terminar """
""" print(frase[15:])  # ==> antes de doi pontos é onde vai começar depois de dois pontos é aonde ele vai terminar """
print(frase[9::3])  # ==> ele vai pular de tres em tres age o final res == vePh """
# Análise
print(len(frase))  # o comando len mostra o comprimento da string
print(frase.count('o'))  # quantas vezes aparece a letra 'o'
print(frase.count('o', 0, 13))  # quantas vezes aparece a letra 'o' com fatiamento res ==> 1 letra o
print(frase.find('deo'))  # a funcao =find() vai me dizer quantas vezes encontrou deo
print(frase.find('android'))  # o res vai ser meno -1 significa nao encontrado ou nao existente
''' 'Curso'in frase  # o (operador)==> in <==( vai perguntar se existe curso em frase) res ==> true '''
# transformações categoria funcionlidade #
print(frase.replace('python', 'android'))   # ''' ==> ( replace significa reposicionar ) entao o caso a onde estiver python ele vai substituir por android. '''
print(frase.upper())   # ''' O comando  ==> upper  <== é um método e como todo metodo ele vai entre upper() ele serve para converter em ==> MAIUSCULAS '''
print(frase.lower())  # '''o comando ==>lower<== converte para minusculas ele também é um método '''
print(frase.capitalize())  # ''' vai pasar todas as caracteristicas e para minusculas com essecao da primeira letra que continuara MAIUSCULAS'''
print(frase.title())  # ''' vai capitalizar palavra por palavra ou seja a primeira letra da frasesempre MAIUSCULA '''
frase.strip()  # ''' o metodo strip() serve para remover os espaçamentos inuteis no começo ou no final de cada frase'''
frase.rstrip()  # para remover o espaçamento da direita ==> adicionar (r)
frase.lstrip()   # para remover o espaçamento da esquerda ==> adicionar (l)
# Divisão: dividindo string
frase.split()  # vai fazer uma divisão considerando os espaços res ==> [curso][em][video][python]
# junção
print('-'.join(frase))  # para separar com traços

