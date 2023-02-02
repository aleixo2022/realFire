import conexao_firebird 
import firebirdSQL_query_produtos_Millennium as fqp
import firebirdSQL_query_produtosEventos_Millennium as fqpe
import firebirdSQL_query_movimento_Millennium as fqm 
import firebirdSQL_query_locaisEstoque_Millennium as fqle
import firebirdSQL_query_transferenciasLocais_Millennium as fqtl

while True:
    con = conexao_firebird.conectar()
    df_fqp = fqp.consulta()
    df_fqpe = fqpe.consulta()
    df_fqm = fqm.consulta()
    df_fqle = fqle.consulta()
    df_fqtl = fqtl.consulta()
    