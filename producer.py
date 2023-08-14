from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:29092')

for i in range(10):
    print('sending message ', i)
    producer.send('ali', b'mensagem- %d' % i)
    print('done')