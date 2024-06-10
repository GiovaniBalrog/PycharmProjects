import mysql.connector  # Importa a biblioteca mysql.connector para conectar ao MySQL
from mysql.connector import Error  # Importa a classe Error para tratar exceções

try:
    # Estabelecer a conexão com o banco de dados
    connection = mysql.connector.connect(
        host='localhost',  # Endereço do servidor MySQL
        database='db_dsa_msql',  # Nome do banco de dados ao qual queremos nos conectar
        user='root',  # Nome de usuário do MySQL
        password=''  # Senha do usuário do MySQL (substitua pela sua senha)
    )

    # Verifica se a conexão foi bem-sucedida
    if connection.is_connected():
        db_info = connection.get_server_info()  # Obtém informações do servidor MySQL
        print("Conectado ao servidor MySQL versão", db_info)

        cursor = connection.cursor()  # Cria um cursor para executar comandos SQL

        # Execute a consulta SQL para selecionar os dados da tabela tb_clientes
        cursor.execute("SELECT * FROM tb_clientes")

        # Obtenha todos os registros da consulta
        records = cursor.fetchall()

        # Imprima os dados da tabela tb_clientes
        print("Dados da tabela tb_clientes:")
        for row in records:
            print("ID_Cliente:", row[0])  # Imprime o ID do cliente
            print("Nome_Cliente:", row[1])  # Imprime o nome do cliente
            print("Cidade:", row[2])  # Imprime a cidade do cliente
            print("Estado:", row[3])  # Imprime o estado do cliente
            print("Pais:", row[4])  # Imprime o país do cliente
            print("Região:", row[5])  # Imprime a região do cliente
            print("Mercado:", row[6])  # Imprime o mercado do cliente
            print("Segmento:", row[7])  # Imprime o segmento do cliente
            print("---------------------------")  # Separa cada registro visualmente

except Error as e:
    # Captura e imprime qualquer erro que ocorrer durante a conexão ou execução das consultas
    print("Erro ao conectar ao MySQL", e)

finally:
    # Garante que a conexão ao banco de dados será fechada
    if connection.is_connected():
        cursor.close()  # Fecha o cursor
        connection.close()  # Fecha a conexão com o banco de dados
        print("Conexão MySQL encerrada")
