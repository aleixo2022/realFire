import conexao_firebird

con = conexao_firebird.conectar()

def consulta(con):
    cur = con.cursor()
    query = """select * from locais_estoque"""
    cur.execute(query)
    return cur.fetchall()
