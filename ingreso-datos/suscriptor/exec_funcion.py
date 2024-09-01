import boto3
import json

client = boto3.client('lambda', region_name='us-east-2')

response = client.invoke(
    FunctionName='latam-lambda-function',
    InvocationType='RequestResponse',
    Payload=json.dumps({})
)

response_payload = json.loads(response['Payload'].read())
print(response_payload)


#Codigo para mantener el contenedor en ejecución