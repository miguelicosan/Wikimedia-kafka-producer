import requests
from confluent_kafka import Producer

url = "https://stream.wikimedia.org/v2/stream/recentchange"
kafka_bootstrap_servers = "127.0.0.1:9092"

# Configuración del productor Kafka
conf = {
    'bootstrap.servers': kafka_bootstrap_servers,
    'client.id': 'wikimedia-producer'
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print('Error en la entrega del mensaje: {}'.format(err))
    else:
        print('Mensaje entregado a {} [{}]'.format(msg.topic(), msg.partition()))

# Función para procesar los cambios recientes y enviarlos a Kafka
def process_recent_changes(data):
    # Aquí puedes personalizar la lógica de procesamiento según tus necesidades
    # En este ejemplo, simplemente enviamos los datos directamente a Kafka
    producer.produce("wikimedia.recentchange", key=None, value=data, callback=delivery_report)
    producer.poll(0)  # Se requiere para que los mensajes se envíen realmente

# Leer la transmisión y procesar los cambios
with requests.get(url, stream=True) as response:
    for line in response.iter_lines():
        if line:
            try:
                decoded_line = line.decode('utf-8')
                process_recent_changes(decoded_line)
            except Exception as e:
                print(f'Error al procesar la línea: {e}')

# Esperar a que todos los mensajes se hayan entregado antes de salir
producer.flush()
