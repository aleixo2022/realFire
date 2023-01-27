# importação dos arquivos
#import conexao_firebird
import kafka_producer
import json
# chamando a função de conexão
#con = conexao_firebird.conectar()

# chamando a função de consulta
#resultados = conexao_firebird.consultar(con, "produtos_eventos")


msg_dict = {
    "operatorId":"Alex",#公交公司ID
    "terminalId":"test",#设备Id
    "terminalCode":"0206",#设备编码（使用车辆ID）
    "terminalNo":"1234",#同一车辆内terminal序号从1开始
}

mensagem = json.dumps(msg_dict).encode()
# chamando a função de envio de mensagem
kafka_producer.enviar_mensagem(mensagem, 'ProdutoEvento')