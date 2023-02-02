import conexao_firebird

con = conexao_firebird.conectar()

def consulta():
     cur = con.cursor()
     query = """select * from transferencias_locais"""
     cur.execute(query)
     return cur.fetchall()
 