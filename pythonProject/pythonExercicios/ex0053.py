
'''
word = input('digite um frase: ')
if str(word) == str(word)[::-1]:
    print('\033[34m{}\033[0m: é palindrome'.format(word))
else:
    print('\033[30m{}\033[0m:não é palindrome'.format(word))
'''
'''
frase = input('digite um frase: ')
if str(frase) == ''.join(reversed(frase)):
    print('\033[34m{}\033[0m: é palindrome'.format(frase))
else:
    print('\033[30m{}\033[0m:não é palindrome'.format(frase))
'''
'''
frase = str(input('digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
 inverso += junto[letra]
if inverso == junto:
         print('\033[34m{},\033[m inverso => \033[31m{}\033[0m: é palindrome'.format(junto, inverso))
else:
    print('\033[30m{},\033[m inverso => \033[31m{}\033[0m:não é palindrome'.format(junto, inverso))
'''

frase = str(input('digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
         print('\033[34m{},\033[m inverso => \033[31m{}\033[0m: é palindrome'.format(junto, inverso))
else:
    print('\033[30m{},\033[m inverso => \033[31m{}\033[0m:não é palindrome'.format(junto, inverso))
