import psycopg2
from psycopg2 import extras
import time
def save_data(mov_estoque, produto, filial, empenho, quantidade, idlocal, tipo_origem, data):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="newport",
            user="postgres",
            password="musica2000"
        )
        
        cursor = connection.cursor()
        
        postgreSQL_insert_query = """INSERT INTO mov_estoque (mov_estoque, produto, filial, empenho, quantidade, idlocal, tipo_origem, data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        
        record_to_insert = (mov_estoque, produto, filial, empenho, quantidade, idlocal, tipo_origem, data)
         
        cursor.execute(postgreSQL_insert_query, record_to_insert)
        
        connection.commit()
        print("dados inseridos com sucesso na tabela")
        
    except(Exception, psycopg2.Error) as error:
        print("Erro ao inserir os dados da mov_estoque do millennium no postgres[mov_estoque]", error)
    
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Consulta encerrada no Postgres!")
   

def check_data_exists(mov_estoque): 
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="newport",
            user="postgres",
            password="musica2000"
        )
        
        cursor = connection.cursor()
        
        postgresSQL_select_query = """SELECT * FROM mov_estoque where mov_estoque = %s"""
        
        cursor.execute(postgresSQL_select_query, (mov_estoque,))
        records = cursor.fetchall()
        
        if len(records) > 0:
            return True
        else:
            return False
    except (Exception, psycopg2.Error) as error:
        print("Não foi possível consultar o id mov_estoque do Banco de dados MIllennium", error)
    
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("2ª consulta no Postgres encerrada com sucesso!")
    