import mysql.connector
from mysql.connector import Error

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='mydb'
        )
        if conexao.is_connected():
            db_info = conexao.get_server_info()
            print(f"Conectado ao servidor MySQL versão {db_info}")
            cursor = conexao.cursor()
            cursor.execute("select database();")
            linha = cursor.fetchone()
            print(f"Conectado ao banco de dados {linha}")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")

def main():
    conexao = criar_conexao()
    if conexao is not None and conexao.is_connected():
        conexao.close()

if __name__ == '__main__':
    main()
