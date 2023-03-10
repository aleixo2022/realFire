import psycopg2


def save_transf(TRANSFERENCIA_LOCAL,COD_TRANSFERENCIA ,DATA ,FILIAL ,TIPO ,STATUS ,USUARIO_INCLUSAO ,DATA_INCLUSAO ,
    USUARIO_ALTERACAO ,DATA_ALTERACAO ,USUARIO_CONFERENCIA ,DATA_CONFERENCIA ,ORIGEM ,TIPO_ORIGEM ,EXCLUIDO ,USUARIO_EXCLUSAO ,
    DATA_EXCLUSAO ,REGRA_WMS ,TRANSFERENCIA_ORIGEM ,STATUS_ORIGINAL ,CRIA_LOTE_CONF_DESTINO ,USUARIO_CONFERENCIA_DESTINO ,SUSPENSO ,
    USUARIO_FINALIZA_SUSPENSO ,DATA_FINALIZA_SUSPENSO ,STATUS_VOLUME ,CONTROLA_VOLUME_ESTOQUE_WMS ,USUARIO_FINALIZACAO ,DATA_FINALIZACAO ,
    DIAS_MINIMOS_VALIDADE_ESTOQUE ,STATUS_WORKFLOW ,STATUS_WORKFLOW_DATE ,TRANSFERENCIA_VOLUME_FECHADO ,REARMAZENAGEM ,ENCADEAMENTO_FINALIZADO ,
    PERSONALIZADO ,BLOQUEADA_PARA_CONFERENCIA ,CONFERENCIA_INDIVIDUAL ,PREPICKING ,IDLOCAL_RAMPA):
     
    
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="newport",
            user="postgres",
            password="musica2000"
        )
        
        cursor = connection.cursor()
        
        postgreSQL_insert_query = """INSERT INTO PRODUTOS (TRANSFERENCIA_LOCAL,COD_TRANSFERENCIA ,DATA ,FILIAL ,TIPO ,STATUS ,USUARIO_INCLUSAO ,DATA_INCLUSAO ,
    USUARIO_ALTERACAO ,DATA_ALTERACAO ,USUARIO_CONFERENCIA ,DATA_CONFERENCIA ,ORIGEM ,TIPO_ORIGEM ,EXCLUIDO ,USUARIO_EXCLUSAO ,
    DATA_EXCLUSAO ,REGRA_WMS ,TRANSFERENCIA_ORIGEM ,STATUS_ORIGINAL ,CRIA_LOTE_CONF_DESTINO ,USUARIO_CONFERENCIA_DESTINO ,SUSPENSO ,
    USUARIO_FINALIZA_SUSPENSO ,DATA_FINALIZA_SUSPENSO ,STATUS_VOLUME ,CONTROLA_VOLUME_ESTOQUE_WMS ,USUARIO_FINALIZACAO ,DATA_FINALIZACAO ,
    DIAS_MINIMOS_VALIDADE_ESTOQUE ,STATUS_WORKFLOW ,STATUS_WORKFLOW_DATE ,TRANSFERENCIA_VOLUME_FECHADO ,REARMAZENAGEM ,ENCADEAMENTO_FINALIZADO ,
    PERSONALIZADO ,BLOQUEADA_PARA_CONFERENCIA ,CONFERENCIA_INDIVIDUAL ,PREPICKING ,IDLOCAL_RAMPA) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
               )"""
     
        record_to_insert = (TRANSFERENCIA_LOCAL,COD_TRANSFERENCIA ,DATA ,FILIAL ,TIPO ,STATUS ,USUARIO_INCLUSAO ,DATA_INCLUSAO ,
    USUARIO_ALTERACAO ,DATA_ALTERACAO ,USUARIO_CONFERENCIA ,DATA_CONFERENCIA ,ORIGEM ,TIPO_ORIGEM ,EXCLUIDO ,USUARIO_EXCLUSAO ,
    DATA_EXCLUSAO ,REGRA_WMS ,TRANSFERENCIA_ORIGEM ,STATUS_ORIGINAL ,CRIA_LOTE_CONF_DESTINO ,USUARIO_CONFERENCIA_DESTINO ,SUSPENSO ,
    USUARIO_FINALIZA_SUSPENSO ,DATA_FINALIZA_SUSPENSO ,STATUS_VOLUME ,CONTROLA_VOLUME_ESTOQUE_WMS ,USUARIO_FINALIZACAO ,DATA_FINALIZACAO ,
    DIAS_MINIMOS_VALIDADE_ESTOQUE ,STATUS_WORKFLOW ,STATUS_WORKFLOW_DATE ,TRANSFERENCIA_VOLUME_FECHADO ,REARMAZENAGEM ,ENCADEAMENTO_FINALIZADO ,
    PERSONALIZADO ,BLOQUEADA_PARA_CONFERENCIA ,CONFERENCIA_INDIVIDUAL ,PREPICKING ,IDLOCAL_RAMPA,)
         
    
        cursor.execute(postgreSQL_insert_query, record_to_insert)
        connection.commit()
        print("Dados inseridos com sucesso!")
    except(Exception, psycopg2.Error) as error:
        print("Error ao inserir dados da tabela transferencias_locais do millennium no Postgres[transferencias_locais]", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Consulta finalizada com sucesso!")
   
def check_transf_exists(TRANSFERENCIA_LOCAL):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="newport",
            user="postgres",
            password="musica2000"
        )
        
        cursor = connection.cursor()
        
        postgresSQL_select_query = """select TRANSFERENCIA_LOCAL,COD_TRANSFERENCIA ,DATA ,FILIAL ,TIPO ,STATUS ,USUARIO_INCLUSAO ,DATA_INCLUSAO ,
    USUARIO_ALTERACAO ,DATA_ALTERACAO ,USUARIO_CONFERENCIA ,DATA_CONFERENCIA ,ORIGEM ,TIPO_ORIGEM ,EXCLUIDO ,USUARIO_EXCLUSAO ,
    DATA_EXCLUSAO ,REGRA_WMS ,TRANSFERENCIA_ORIGEM ,STATUS_ORIGINAL ,CRIA_LOTE_CONF_DESTINO ,USUARIO_CONFERENCIA_DESTINO ,SUSPENSO ,
    USUARIO_FINALIZA_SUSPENSO ,DATA_FINALIZA_SUSPENSO ,STATUS_VOLUME ,CONTROLA_VOLUME_ESTOQUE_WMS ,USUARIO_FINALIZACAO ,DATA_FINALIZACAO ,
    DIAS_MINIMOS_VALIDADE_ESTOQUE ,STATUS_WORKFLOW ,STATUS_WORKFLOW_DATE ,TRANSFERENCIA_VOLUME_FECHADO ,REARMAZENAGEM ,ENCADEAMENTO_FINALIZADO ,
    PERSONALIZADO ,BLOQUEADA_PARA_CONFERENCIA ,CONFERENCIA_INDIVIDUAL ,PREPICKING ,IDLOCAL_RAMPA from transferencias_locais where transferencia_local = %s"""
        
        cursor.execute(postgresSQL_select_query, (TRANSFERENCIA_LOCAL,))
        records = cursor.fetchall()
        
        if len(records) > 0:
            return True
        else:
            return False
    except(Exception, psycopg2.Error) as error:
        print("N??o foi poss??vel consultar o id transferencia_local do banco de dados MIllennium", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("2?? consulta no postgres encerrada com sucesso!")
        
