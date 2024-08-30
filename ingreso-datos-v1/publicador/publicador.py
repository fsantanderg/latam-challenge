import boto3, time, logging
from datetime import datetime


# Configurar la correcta región de SNS según corresponda
sns_client = boto3.client('sns', region_name='us-east-2')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def publish_message(message, topic_arn):
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message
    )
    print(f"ID Mensaje: {response['MessageId']}")
    logging.info(f"ID Mensaje: {response['MessageId']}")

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = f"Este es un mensaje de prueba para el Challenge Latam. Fecha y hora: {current_datetime}"

try:
    while True:
        publish_message(message, "arn:aws:sns:us-east-2:111111111111:data-ingestion-topic")
        time.sleep(3)  # Espera 3 segundos antes de la siguiente ejecución
except KeyboardInterrupt:
    print("El ciclo ha sido detenido manualmente.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
