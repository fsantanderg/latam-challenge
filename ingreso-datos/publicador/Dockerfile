FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN apt update && apt upgrade -y && apt install htop -y && apt install curl -y
RUN pip install --no-cache-dir -r requirements.txt

COPY publicador.py .

EXPOSE 8000

CMD ["uvicorn", "publicador:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]


#docker run -it -v ./:/app -p 8000:8000 python:3.9-slim /bin/bash


####DOCKER HUB
#docker build -t fsantanderg/latam_publisher:1.0.4 .
#docker push fsantanderg/latam_publisher:1.0.4
#docker run -d fsantanderg/latam_publisher:1.0.0