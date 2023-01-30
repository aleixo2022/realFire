# importação dos arquivos
import conexao_firebird
import kafka_producer
import json
import time

while True:
    #chamando a função de conexão
    con = conexao_firebird.conectar()

    #chamando a função de consulta
    resultados = conexao_firebird.consultar(con, "produtos_eventos")
  
    # mensagem = {
    #     "operatorId":"tete01",  
    #     "terminalId":"test", 
    #     "terminalCode":"0206", 
    #     "terminalNo":"1234", 
    # }

    print(resultados)
    # mensagem = json.dumps(mensagem).encode()
    # print(mensagem)
    # chamando a função de envio de mensagem
    # kafka_producer.enviar_mensagem(mensagem, 'ProdutoEvento')
    time.sleep(5)