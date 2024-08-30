FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY suscriptor.py .

CMD ["python", "suscriptor.py"]


# Construir la imagen Docker
#docker build -t latam_suscriptor .

# Etiquetar la imagen
#docker tag latam_suscriptor:latest 111111111111.dkr.ecr.us-east-2.amazonaws.com/latam_suscriptor:latest

# Subir la imagen a ECR
#docker push 111111111111.dkr.ecr.us-east-2.amazonaws.com/latam_suscriptor:latest