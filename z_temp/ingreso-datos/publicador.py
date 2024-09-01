import boto3
from datetime import datetime


# Configurar la correcta región de SNS según corresponda
sns_client = boto3.client('sns', region_name='us-east-2')

def publish_message(message, topic_arn):
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message
    )
    print(f"Message ID: {response['MessageId']}")

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = f"Este es un mensaje de prueba para el Challenge Latam. Fecha y hora: {current_datetime}"

publish_message(message, "arn:aws:sns:us-east-2:111111111111:data-ingestion-topic")
