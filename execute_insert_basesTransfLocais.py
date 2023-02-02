import conexao_firebird 
import firebirdSQL_query_transferenciasLocais_Millennium  


while True:
    con = conexao_firebird.conectar()
    firebirdSQL_query_transferenciasLocais_Millennium.consulta(con)