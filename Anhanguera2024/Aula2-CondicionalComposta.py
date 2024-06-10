# Solicitar a temperatura
temperatura_str = input("Quantos graus está fazendo hoje? :")

# Verificar se o usuário forneceu uma entrada válida e fazer a conversão para inteiro
temperatura = int(temperatura_str) if temperatura_str.strip() else None

# Verificar a temperatura usando uma estrutura condicional composta
mensagem = (
    "Está quente!" if temperatura and temperatura >= 30
    else "Está agradável." if temperatura and 10 < temperatura <= 29
    else "Está frio." if temperatura and temperatura <= 10
    else "Digite um valor válido."
)

print(mensagem)

"""" é uma estrutura condicional composta em uma única linha, que faz o seguinte:

Verifica se temperatura_str.strip() retorna True (ou seja, se a string não está vazia após remover espaços em branco).
Se a condição for True, converte temperatura_str para um número inteiro usando int(temperatura_str).
Caso contrário, se a condição for False (ou seja, se a string estiver vazia), atribui None à variável temperatura.
Essa é uma maneira compacta e eficiente de lidar com a conversão de uma string para um número inteiro, com a adição da lógica de verificar se a string não está vazia antes da conversão.

Se precisar de mais alguma explicação ou tiver outras dúvidas, estou à disposição para ajudar! """