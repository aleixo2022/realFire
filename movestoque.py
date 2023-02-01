import connectModules.conexao_firebird as conexao_firebird
import pandas as pd
con = conexao_firebird.conectar()

def consultar(con, tabela):
    cur = con.cursor()
    cur.execute("select mov_estoque, produto,  filial, empenho, quantidade,idlocal,tipo_origem, data from "+ tabela +" where produto in(7156458,3320309)")    
    return cur.fetchall()

 