import conexao_firebird 
import firebirdSQL_query_produtos_Millennium  
import firebirdSQL_query_produtosEventos_Millennium as fqpe
import firebirdSQL_query_movimento_Millennium as fqm 
import firebirdSQL_query_locaisEstoque_Millennium as fqle
import firebirdSQL_query_transferenciasLocais_Millennium as fqtl


while True:
    con = conexao_firebird.conectar()
    df_fqp = firebirdSQL_query_produtos_Millennium.consulta(con)

    