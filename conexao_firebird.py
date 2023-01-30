import fdb
import pandas as pd
def conectar():
    # informações de conexão
    host = "10.255.255.115" #10.20.4.179"
    banco = "c:/BD/DESENVOLVIMENTO.FDB"#D:/Sys/Base/MILLENNIUM"
    usuario = "sysdba"
    senha = "masterkey"
    
    # criação da conexão
    con = fdb.connect(
        host=host,
        database=banco,
        user=usuario,
        password=senha
    )
    return con

def consultar(con, tabela):
    # criação do cursor
    cur = con.cursor()
    
    # consulta
    query =pd.read_sql("SELECT  * FROM  " + tabela +" where data > '01.01.2022'", con)
    
    # fechamento do cursor
    cur.close()
    
    return query