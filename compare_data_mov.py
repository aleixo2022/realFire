import pandas as pd 
import connectModules.connect_postgres as pqm
import connectModules.conexao_firebird as fqm
import consulteBD.firebirdSQL_query_mov_Millennium as fqmQuery
import consulteBD.postgresSQL_query_mov as pqmQuery

queryPqm = pqm.connect()

queryFqm = fqm.conectar()

fqmData = fqmQuery.consulta()

result = pd.DataFrame(fqmData, columns=['mov_estoque', 'produto',  'filial', 'empenho', 'quantidade','idlocal','tipo_origem','data'])

print(result)
