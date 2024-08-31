import boto3
import psycopg2
import json
import os

# Configurar el cliente SQS con la región correcta
sqs_client = boto3.client('sqs', region_name='us-east-2')
queue_url = os.getenv('SQS_QUEUE_URL')

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
            original_message = body.get('Message')
            process_message(original_message)
            sqs_client.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )

def process_message(message_body):
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')

    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO ingresar_datos (datos) VALUES (%s)", (message_body,))
    conn.commit()
    cur.close()
    conn.close()

process_messages()
