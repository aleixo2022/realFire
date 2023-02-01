import sys
sys.path.append("C:/Apache/realFire/consulteBD")
import connectModules.conexao_firebird as conexao_firebird
con = conexao_firebird.conectar()

def consulta():
    
    query = """select mov_estoque, produto, filial, empenho, quantidade, idlocal, tipo_origem, data from mov_estoque """
    con.execute(query)
    return con.fetchall()