import connect_postgres as connect_postgres
con = connect_postgres.connect()

def consulta():
    
    query = """select mov_estoque, produto, filial, empenho, quantidade, idlocal, tipo_origem, data from mov_estoque """
    con.execute(query)
    return con.fetchall()