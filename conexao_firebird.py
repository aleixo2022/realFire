import fdb

def conectar():
    # informações de conexão
    host = "10.20.4.179"
    banco = "D:/Sys/Base/MILLENNIUM"
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
    query = "SELECT max(cod_operacao) FROM  " + tabela
    cur.execute(query)
    
    # obtenção dos resultados
    resultados = cur.fetchall()
    
    # fechamento do cursor
    cur.close()
    
    return resultados