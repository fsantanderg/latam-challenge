# latam-challenge

#Infraestructura e IaC
## 1.
Para utilizar el esquema PUB/SUB, se considerará la utilización de los siguientes servicios:

### A.
 - Amazon Simple Notification Service (ASNS), quien recibira los mensajes generados
 - Amazon SQS, quien se encargara de procesar los mensajes

### B.
Se considero una base de datos Postgres
 - En la siguiente ruta "helm-charts\postgres-citus" se encuentran los helm-chart para montar la base de datos en kubernetes
 - Wn la siguiente ruta "terraform\db_postgres" se encuentran los código terraform para levantar una base de datos con el servicio de RDS de AWS.

### C.
 - 


## Creación de la infraestrcutra principal a montar la solución en un Cluster de Kubernetes




 - Instalación de CRD necesarios para validar y actualizar certificados SSL automaticamente
 kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.11.1/cert-manager.crds.yaml