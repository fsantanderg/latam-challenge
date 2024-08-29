import boto3
import psycopg2
import json

# Configura el cliente SQS con la región correcta
sqs_client = boto3.client('sqs', region_name='us-east-2')
queue_url = 'https://sqs.us-east-2.amazonaws.com/111111111111/data-processing-queue'

def process_messages():
    while True:
        messages = sqs_client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20
        )
        
        for message in messages.get('Messages', []):
            # Parsear el JSON recibido
            body = json.loads(message['Body'])
            original_message = body.get('Message')  # Extraer el contenido del mensaje original
            process_message(original_message)
            sqs_client.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )

def process_message(message_body):
    # Ingresar los datos de acceso a base de datos PostgreSQL
    conn = psycopg2.connect("dbname=latam user=latam_user password=latam_password host=localhost")
    cur = conn.cursor()
    cur.execute("INSERT INTO ingresar_datos (datos) VALUES (%s)", (message_body,))
    conn.commit()
    cur.close()
    conn.close()

process_messages()
