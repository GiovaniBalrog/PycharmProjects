#Exercício 5 – Antecessor e Sucessor
n = int(input('Diga um numero: '))
# Utilizando tres variáveis.
#b = n+1
#c = n-1
#print('seu numero é: {} \n {} ==> É successor \n {} ==> É o antecessor'. format(n, b, c))
#===================>>>>> ultulizando apenas uma variavel.
print('seu numero é: {} \n {} ==> É successor \n {} ==> É o antecessor'. format(n, (n+1), (n-1)))