import pika
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s\n\n",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def payload_handle(ch, method, properties, body):
    # canal gerado
    logging.info("Parametro 1: %s", ch)
    
    # informacoes da comunicacao com o broker
    logging.info("Parametro 2: %s", method)

    # modo de entrega (armazenado em memoria ou disco) e headers de configuracao adicional
    logging.info("Parametro 3: %s", properties)

    # mensagem completa
    logging.info("Mensagem recebida do Broker: %s", body.decode())

connection_params = pika.URLParameters('amqp://localhost:5672')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

queue_name = 'categorias-fifo'
channel.queue_declare(queue=queue_name, durable=True)

channel.basic_consume(queue=queue_name, on_message_callback=payload_handle, auto_ack=True)

print(f'Waiting for messages on the "{queue_name}" queue. To exit, press CTRL+C')
channel.start_consuming()
