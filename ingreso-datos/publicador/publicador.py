from fastapi import FastAPI, HTTPException
import asyncpg
from pydantic import BaseModel
import boto3, logging
from datetime import datetime
from threading import Thread, Event

# Inicializar FastAPI
app = FastAPI()

DATABASE_URL = "postgresql://latam_user:latam_password@localhost/latamdb"

# Conectar a la base de datos
async def get_db_pool():
    return await asyncpg.create_pool(DATABASE_URL)

# Configurar la correcta región de SNS según corresponda
sns_client = boto3.client(
    'sns',
    region_name='us-east-2',
    aws_access_key_id='111111111111',
    aws_secret_access_key='111111111111111111111111'
)

# Configuración básica del logger para enviar logs a la consola estándar
logging.basicConfig(
    level=logging.INFO,  # Nivel de log
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del log
)

# Modelo para la solicitud POST
class MessageRequest(BaseModel):
    topic_arn: str
    message: str

def publish_message(message, topic_arn, result, event):
    try:
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message
        )
        logging.info(f"Transaction ID: {response['MessageId']}")
        result["message_id"] = response['MessageId']
    except Exception as e:
        logging.error(f"Ocurrió un error inesperado: {e}")
        result["message_id"] = None
    finally:
        event.set()  # Indicar que el hilo ha terminado

@app.post("/ingresar-datos/")
def start_publishing_endpoint(request: MessageRequest):
    try:
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = request.message + ". Fecha y hora: " + current_datetime

        # Asumiendo que request.topic_arn es solo el nombre del tópico y no el ARN completo
        topic_arn = f"arn:aws:sns:us-east-2:111111111111:{request.topic_arn}"

        result = {}
        event = Event()
        thread = Thread(target=publish_message, args=(message, topic_arn, result, event))
        thread.start()
        event.wait()  # Esperar a que el hilo indique que ha terminado

        if result["message_id"]:
            return {"status": "Publicación OK", "transaction_id": result["message_id"]}
        else:
            raise HTTPException(status_code=500, detail="Error al publicar el mensaje")
    except Exception as e:
        logging.error(f"Ocurrió un error inesperado: {e}")
        raise HTTPException(status_code=500, detail=f"500: {str(e)}")

@app.get("/data/{item_id}")
async def read_data(item_id: int):
    pool = await get_db_pool()
    async with pool.acquire() as connection:
        row = await connection.fetchrow("SELECT * FROM ingresar_datos WHERE id = $1", item_id)
        if row:
            return {"id": row["id"], "datos": row["datos"]}
        else:
            raise HTTPException(status_code=404, detail="Item not found")


#Para ejecutar el servidor de desarrollo, ejecutar el siguiente comando:
#uvicorn publicador:app --reload --host 0.0.0.0 --port 8000