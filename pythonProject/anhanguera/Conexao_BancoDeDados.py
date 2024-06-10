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

        # Execute a consulta SQL para obter o nome do banco de dados atualmente conectado
        cursor.execute("SELECT DATABASE();")

        # Obtenha o resultado da consulta
        record = cursor.fetchone()

        # Imprima o nome do banco de dados conectado
        print("Conectado ao banco de dados:", record)

except Error as e:
    # Captura e imprime qualquer erro que ocorrer durante a conexão ou execução das consultas
    print("Erro ao conectar ao MySQL", e)

finally:
    # Garante que a conexão ao banco de dados será fechada
    if connection.is_connected():
        cursor.close()  # Fecha o cursor
        connection.close()  # Fecha a conexão com o banco de dados
        print("Conexão MySQL encerrada")

