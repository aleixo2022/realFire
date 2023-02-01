#importação dos arquivos
import models.conexao_firebird as conexao_firebird
import movestoque
#import kafka_producer
import time
import pandas as pd
from db_operations import save_data, check_data_exists
import numpy as np
contador = 0
while True:
    #chamando a função de conexão
    con = conexao_firebird.conectar()

    #chamando a função de consulta
    resultados = movestoque.consultar(con, "mov_estoque")
    
    dfmov= pd.DataFrame(resultados, columns=['mov_estoque', 'produto',  'filial', 'empenho', 'quantidade','idlocal','tipo_origem','data'])
    num_rows = dfmov.shape[0]
    dfmov['data'] = pd.to_datetime(dfmov['data'])
    dfmov['data'] = dfmov['data'].dt.date.astype(str)
    dfmov = dfmov.replace(np.nan, None, regex=True)
    for index, row in dfmov.iterrows():       
        mov_estoque = row['mov_estoque']    
        
        if not check_data_exists(mov_estoque):
            save_data(row['mov_estoque'], row['produto'],row['filial'],row['empenho'],row['quantidade'],row['idlocal'],row['tipo_origem'],row['data']),
        contador = contador + 1
        with open('cont.txt', 'w') as file:
            file.write(str(contador))
        file.close()
        if contador == num_rows:
            break
    time.sleep(60)    
    # chamando a função de envio de mensagem
    #kafka_producer.enviar_mensagem(mensagem, 'npestoque')
    
