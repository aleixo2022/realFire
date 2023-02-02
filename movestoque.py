import pandas as pd 
import numpy as np
from db_operations import save_data, check_data_exists
 
contador = 0

def consultar(con):
    cur = con.cursor()
    cur.execute("select mov_estoque, produto,  filial, empenho, quantidade,idlocal,tipo_origem, data from  mov_estoque")    
    resultados = cur.fetchall()
    dfmov= pd.DataFrame(resultados, columns=['mov_estoque', 'produto',  'filial', 'empenho', 'quantidade','idlocal','tipo_origem','data'])
   
    dfmov['data'] = pd.to_datetime(dfmov['data'])
    dfmov['data'] = dfmov['data'].dt.date.astype(str)
    dfmov = dfmov.replace(np.nan, None, regex=True)
    
    num_rows = dfmov.shape[0]  
   
    for index, row in dfmov.iterrows():       
        mov_estoque = row['mov_estoque']    
        
        if not check_data_exists(mov_estoque):
            save_data(row['mov_estoque'], row['produto'],row['filial'],row['empenho'],row['quantidade'],row['idlocal'],row['tipo_origem'],row['data']),
        
        with open('cont.txt', 'w') as file:
            file.write(str(contador))
        file.close()
        if contador == num_rows:
            break