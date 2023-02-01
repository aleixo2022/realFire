import pandas as pd 
import firebirdSQL_query_mov_Millennium as fqmQuery
import postgresSQL_query_mov as pqmQuery

pqmData = pqmQuery.consulta()

fqmData = fqmQuery.consulta()

result = pd.DataFrame(pqmData, columns=['mov_estoque', 'produto',  'filial', 'empenho', 'quantidade','idlocal','tipo_origem','data'])

print(result)
