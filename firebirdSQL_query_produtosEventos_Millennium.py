import conexao_firebird as conexao_firebird
import pandas as pd 
con = conexao_firebird.conectar()

def consulta():
    cur = con.cursor()
    query = """select * from produtos_eventos"""
    cur.execute(query)
    return cur.fetchall()

