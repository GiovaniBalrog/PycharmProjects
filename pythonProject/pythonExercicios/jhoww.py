def celsius(c=0):
    con1 = c + 273
    con2 = (c * 9.) / 5. + 32
    print(" A conversao em Kelvin: %dK" % con1)
    print(" A conversao em Fahrenheit: %.2fF" % con2)


def kelvin(k=0):
    con3 = k - 273
    con4 = ((k - 273) / 5.) * 9. + 32
    print(" A conversao em Celsius: %.2fC" % con3)
    print(" A conversao em Fahrenheit: %.2fF" % con4)


def fahrenheit(f=0):
    con5 = ((f - 32) / 9.) * 5.


    con6 = ((f - 32) / 9.) * 5. + 273
    print(" A conversao em Celsius: %.2fC" % con5)
    print(" A conversao em Kelvin: %.2fK" % con6)



print("  Conversor de Temperaturas: Celsius, Kelvin e Fahrenheit!")
print("============================================================")
print("Escolha uma das alternativas e tecle enter")
print("\n")
print("        1. Celsius para kelvin e Fahrenheit")
print("        2. Kelvin para Celsius e Fahrenheit")
print("        3. Fahrenheit para kelvin e Celsius")
print("\n")
print("        4. Sair deste programa")
print("===========================================================")

x = int(input())

if x == 1:
    celsius(int(input('Digite um valor em Celsius: ')))
elif x == 2:
    kelvin(int(input('Digite um valor em Kelvin: ')))
elif x == 3:
    fahrenheit(int(input('Digite um valor em Fahrenheit: ')))
elif x == 4:
    print("Saindo...")
    pass
exit()