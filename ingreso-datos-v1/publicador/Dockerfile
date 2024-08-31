FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY publicador.py .

CMD ["python", "publicador.py"]

# Construir la imagen Docker
#docker build -t latam_publicador .

# Etiquetar la imagen
#docker tag latam_publicador:latest 111111111111.dkr.ecr.us-east-2.amazonaws.com/latam_publicador:latest

# Subir la imagen a ECR
#docker push 111111111111.dkr.ecr.us-east-2.amazonaws.com/latam_publicador:latest