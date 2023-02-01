import pandas as pd 
import firebirdSQL_query_mov_Millennium as fqmQuery
import postgresSQL_query_mov as pqmQuery

pqmData = pqmQuery.consulta()

fqmData = fqmQuery.consulta()

dfmov1 = pd.DataFrame(fqmData, columns=['mov_estoque', 'produto',  'filial', 'empenho', 'quantidade','idlocal','tipo_origem','data'])
dfmov2 = pd.DataFrame(pqmData, columns=['mov_estoque', 'produto',  'filial', 'empenho', 'quantidade','idlocal','tipo_origem','data'])

not_in_dfmov2 = dfmov1[~dfmov1['mov_estoque'].isin(dfmov2['mov_estoque'])]
not_in_dfmov2.to_csv("base_inexistente.csv", index=False)
dfmov1.to_csv("dfmov1.csv", index=False)
dfmov2.to_csv("dfmov2.csv", index=False)

print(not_in_dfmov2)
