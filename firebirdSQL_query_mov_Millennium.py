import conexao_firebird as conexao_firebird
import pandas as pd
con = conexao_firebird.conectar()

def consulta():
    cur = con.cursor()
    query = """select mov_estoque, produto, filial, empenho, quantidade, idlocal, tipo_origem, data from mov_estoque """
    cur.execute(query)
    return cur.fetchall()