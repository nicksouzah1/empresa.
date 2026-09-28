import mysql.connector


def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="empresa"
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar no banco: {erro}")
        print("Verifique se o MySQL está rodando e se o banco 'empresa' existe.")
        return None
