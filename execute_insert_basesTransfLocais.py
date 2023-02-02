import conexao_firebird 
import firebirdSQL_query_produtos_Millennium  
import firebirdSQL_query_produtosEventos_Millennium as fqpe
import firebirdSQL_query_movimento_Millennium as fqm 
import firebirdSQL_query_locaisEstoque_Millennium as fqle
import firebirdSQL_query_transferenciasLocais_Millennium  


while True:
    con = conexao_firebird.conectar()
    firebirdSQL_query_transferenciasLocais_Millennium.consulta(con)