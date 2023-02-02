import pandas as pd 
import numpy as np
from db_operationsTransfLocais import check_transf_exists, save_transf

contador = 0
def consulta(con):
     
    cur = con.cursor()    
    cur.execute("""select TRANSFERENCIA_LOCAL,COD_TRANSFERENCIA ,DATA ,FILIAL ,TIPO ,STATUS ,USUARIO_INCLUSAO ,DATA_INCLUSAO ,
    USUARIO_ALTERACAO ,DATA_ALTERACAO ,USUARIO_CONFERENCIA ,DATA_CONFERENCIA ,ORIGEM ,TIPO_ORIGEM ,EXCLUIDO ,USUARIO_EXCLUSAO ,
    DATA_EXCLUSAO ,REGRA_WMS ,TRANSFERENCIA_ORIGEM ,STATUS_ORIGINAL ,CRIA_LOTE_CONF_DESTINO ,USUARIO_CONFERENCIA_DESTINO ,SUSPENSO ,
    USUARIO_FINALIZA_SUSPENSO ,DATA_FINALIZA_SUSPENSO ,STATUS_VOLUME ,CONTROLA_VOLUME_ESTOQUE_WMS ,USUARIO_FINALIZACAO ,DATA_FINALIZACAO ,
    DIAS_MINIMOS_VALIDADE_ESTOQUE ,STATUS_WORKFLOW ,STATUS_WORKFLOW_DATE ,TRANSFERENCIA_VOLUME_FECHADO ,REARMAZENAGEM ,ENCADEAMENTO_FINALIZADO ,
    PERSONALIZADO ,BLOQUEADA_PARA_CONFERENCIA ,CONFERENCIA_INDIVIDUAL ,PREPICKING ,IDLOCAL_RAMPA from transferencias_locais""")
    resultados = cur.fetchall()
    
    dfprod = pd.DataFrame(resultados, columns=['TRANSFERENCIA_LOCAL','COD_TRANSFERENCIA','DATA','FILIAL','TIPO','STATUS','USUARIO_INCLUSAO',
                                               'DATA_INCLUSAO','USUARIO_ALTERACAO','DATA_ALTERACAO','USUARIO_CONFERENCIA','DATA_CONFERENCIA',
                                               'ORIGEM','TIPO_ORIGEM','EXCLUIDO','USUARIO_EXCLUSAO','DATA_EXCLUSAO','REGRA_WMS','TRANSFERENCIA_ORIGEM',
                                               'STATUS_ORIGINAL','CRIA_LOTE_CONF_DESTINO','USUARIO_CONFERENCIA_DESTINO','SUSPENSO','USUARIO_FINALIZA_SUSPENSO',
                                               'DATA_FINALIZA_SUSPENSO','STATUS_VOLUME','CONTROLA_VOLUME_ESTOQUE_WMS','USUARIO_FINALIZACAO','DATA_FINALIZACAO',
                                               'DIAS_MINIMOS_VALIDADE_ESTOQUE','STATUS_WORKFLOW','STATUS_WORKFLOW_DATE','TRANSFERENCIA_VOLUME_FECHADO',
                                               'REARMAZENAGEM','ENCADEAMENTO_FINALIZADO','PERSONALIZADO','BLOQUEADA_PARA_CONFERENCIA','CONFERENCIA_INDIVIDUAL',
                                               'PREPICKING','IDLOCAL_RAMPA'])
    
    # dfprod['DATA_ATUALIZACAO'] = pd.to_datetime(dfprod['DATA_CADASTRO'])
    # dfprod['DATA_ATUALIZACAO'] = dfprod['DATA_ATUALIZACAO'].dt.date.stype(str)
    dfprod = dfprod.replace(np.nan, None, regex=True)
    
    num_rows = dfprod.shape[0]
    
    for index, row in dfprod.iterrows():
        trasnf = row['TRANSFERENCIA_LOCAL']
         
        if not check_transf_exists(trasnf):
            save_transf(row['TRANSFERENCIA_LOCAL'],row['COD_TRANSFERENCIA'],row['DATA'],row['FILIAL'],row['TIPO'],row['STATUS'],row['USUARIO_INCLUSAO'],row['DATA_INCLUSAO'],row['USUARIO_ALTERACAO'],row['DATA_ALTERACAO'],row['USUARIO_CONFERENCIA'],row['DATA_CONFERENCIA'],row['ORIGEM'],row['TIPO_ORIGEM'],row['EXCLUIDO'],row['USUARIO_EXCLUSAO'],row['DATA_EXCLUSAO'],row['REGRA_WMS'],row['TRANSFERENCIA_ORIGEM'],row['STATUS_ORIGINAL'],row['CRIA_LOTE_CONF_DESTINO'],row['USUARIO_CONFERENCIA_DESTINO'],row['SUSPENSO'],row['USUARIO_FINALIZA_SUSPENSO'],row['DATA_FINALIZA_SUSPENSO'],row['STATUS_VOLUME'],row['CONTROLA_VOLUME_ESTOQUE_WMS'],row['USUARIO_FINALIZACAO'],row['DATA_FINALIZACAO'],row['DIAS_MINIMOS_VALIDADE_ESTOQUE'],row['STATUS_WORKFLOW'],row['STATUS_WORKFLOW_DATE'],row['TRANSFERENCIA_VOLUME_FECHADO'],row['REARMAZENAGEM'],row['ENCADEAMENTO_FINALIZADO'],row['PERSONALIZADO'],row['BLOQUEADA_PARA_CONFERENCIA'],row['CONFERENCIA_INDIVIDUAL'],row['PREPICKING'],row['IDLOCAL_RAMPA'])
        with open('cont.txt', 'w') as file:
            file.write(str(contador))
        file.close()
        if contador == num_rows:
            break