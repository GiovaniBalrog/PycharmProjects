#Exercício 4 – Dissecando uma Variável
a = input('Digite algo')
print('O tipo primitivo desse valor é', type(a))
print('só temespaços?', a.isspace())
print('é um numero?', a.isnumeric())
print('é alfabetico?', a.isalpha())
print('é alfanumerico?', a.isalnum())
print('esta em maiusculas?', a.isupper())
print('esta em minusculas?', a.islower())
print('esta capitalizada?', a.istitle())
