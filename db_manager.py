import mysql.connector
from mysql.connector import Error



def criar_conexao():
    """Cria uma conexão com o banco de dados."""
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='QuotesDatabase'
        )
        print("Banco Conectado com sucesso!")
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


def inserir_quote(origin: object, language: object, currency: object, date: object, accountmanager: object, companyname: object, contactname: object, companytype: object, companycountry: object,
                  companystate: object,
                  companycity: object, paymenterm: object, freight: object, totalamount: object) -> object:
    """Insere um novo registro na tabela QuoteSent."""
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        query = ("INSERT INTO QuoteSent (Origin, Language, Currency, Date, AccountManager, CompanyName, ContactName, CompanyType, CompanyCountry, CompanyState, CompanyCity, "
                 "PaymentTerm, Freight, TotalAmount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        valores = (origin, language, currency, date, accountmanager, companyname, contactname, companytype, companycountry, companystate,
                  companycity, paymenterm, freight, totalamount)
        cursor.execute(query, valores)
        conexao.commit()
        print(f"Quote adicionada com sucesso. ID: {cursor.lastrowid}")

    except Error as e:
        print(f"Erro ao inserir quote: {e}, conexão com banco nao estabalecida")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


def consultar_quotes():
    """Consulta todos os registros na tabela QuoteSent."""
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        query = "SELECT * FROM QuoteSent"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for linha in resultados:
            print(linha)
    except Error as e:
        print(f"Erro ao consultar quotes: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


def deletar_quote(id_quote):
    """Deleta um registro específico da tabela QuoteSent pelo idQuoteSent."""
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        query = "DELETE FROM QuoteSent WHERE idQuoteSent = %s"
        cursor.execute(query, (id_quote,))
        conexao.commit()
        print(f"Quote com ID {id_quote} deletada com sucesso.")
    except Error as e:
        print(f"Erro ao deletar quote: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


# Exemplos de uso
#if __name__ == '__main__':
    # Inserir uma nova quote
    #inserir_quote('EPS Americana', 'BRL', 'Wellyson', 'Compwire',
                #  'Murilo Rupp', 'System Integrator', 'Brasil', 'Santa Catarina', 'Florianapolis','NET30',
                 # 'Sedex', 17800)

    # Consultar todas as quotes
    # consultar_quotes()

    # Deletar uma quote pelo ID
    # deletar_quote(1)
