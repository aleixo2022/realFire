# importação dos arquivos
#import conexao_firebird
import kafka_producer
import json
# chamando a função de conexão
#con = conexao_firebird.conectar()

# chamando a função de consulta
#resultados = conexao_firebird.consultar(con, "produtos_eventos")


msg_dict = {
    "operatorId":"tete01", 
    "terminalId":"test", 
    "terminalCode":"0206", 
    "terminalNo":"1234", 
}

mensagem = json.dumps(msg_dict).encode()
# chamando a função de envio de mensagem
kafka_producer.enviar_mensagem(mensagem, 'ProdutoEvento')