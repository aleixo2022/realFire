from kafka import KafkaProducer
 
def enviar_mensagem(mensagem, topico):
    print(mensagem)
    # configuração do producer
    producer = KafkaProducer(bootstrap_servers='10.255.255.115:9092')
    
    # envio da mensagem
    producer.send(topico, mensagem)
    
    # fechamento do producer
    