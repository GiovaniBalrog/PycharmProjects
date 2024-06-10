c = float(input('Qual a temperatura de ºC: '))
f = 9 * c / 5 + 32
k = - 273.15
k = c - k

print('A temperatura de {}ºC ==> celsius corresponde \n{}ºF ==> fahrenheit  \n{}ºK ==> kelvin '. format(c, f, k))