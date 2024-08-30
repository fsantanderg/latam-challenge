from fastapi import FastAPI, HTTPException
import asyncpg
from pydantic import BaseModel
import boto3, logging, time
from datetime import datetime
from threading import Thread

# Inicializar FastAPI
app = FastAPI()

DATABASE_URL = "postgresql://latam_user:latam_password@localhost/latamdb"

# Conectar a la base de datos
async def get_db_pool():
    return await asyncpg.create_pool(DATABASE_URL)

# Configurar la correcta región de SNS según corresponda
sns_client = boto3.client('sns', region_name='us-east-2')

# Configuración básica del logger para enviar logs a la consola estándar
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Modelo para la solicitud POST
class MessageRequest(BaseModel):
    topic_arn: str
    message: str

def publish_message(message, topic_arn):
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message
    )
    logging.info(f"Message ID: {response['MessageId']}")

def start_publishing(topic_arn, message):
    try:
            publish_message(message, topic_arn)
    except KeyboardInterrupt:
        logging.info("El ciclo ha sido detenido manualmente.")
    except Exception as e:
        logging.error(f"Ocurrió un error inesperado: {e}")

@app.post("/ingresar-datos/")
def start_publishing_endpoint(request: MessageRequest):
    try:
        # Iniciar el proceso en un hilo separado
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = request.message + ". Fecha y hora: " + current_datetime
        thread = Thread(target=start_publishing, args=("arn:aws:sns:us-east-2:825483337283:" + request.topic_arn, message))
        thread.start()
        return {"status": "Se inició la publicación"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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
#uvicorn main:app --reload