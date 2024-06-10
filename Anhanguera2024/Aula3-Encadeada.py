# Solicitar a temperatura
temperatura_str = input("Quantos graus está fazendo hoje? :")

# Verificar se o usuário forneceu uma entrada válida
if temperatura_str.strip():  # Verifica se a entrada não está vazia
    temperatura = int(temperatura_str)  # Converte a entrada para um número inteiro

    # Verificar a temperatura usando uma estrutura condicional encadeada
    if temperatura >= 30:
        print("Está quente!")
    elif 10 < temperatura <= 29:
        print("Está agradável.")
    elif temperatura <= 10:
        print("Está frio.")
else:
    print("Digite um valor válido.")  # Se o usuário não digitar um valor, imprime "Digite um valor válido."
