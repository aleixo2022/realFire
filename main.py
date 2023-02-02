#importação dos arquivos
import  conexao_firebird as conexao_firebird
import movestoque
#import kafka_producer
import time

while True:
    #chamando a função de conexão
    con = conexao_firebird.conectar()

    #chamando a função de consulta
    dfmov = movestoque.consultar(con)
   
    time.sleep(60)    
    # chamando a função de envio de mensagem
    #kafka_producer.enviar_mensagem(mensagem, 'npestoque')
    
