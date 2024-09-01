# latam-challenge

#Infraestructura e IaC
##1.A
Para utilizar el esquema PUB/SUB, se considerará la utilización de los siguientes servicios:
 - Amazon Simple Notification Service (ASNS), quien recibira los mensajes generados
 - Amazon SQS, quien se encargara de procesar los mensajes

# Parte 1 - Infraestructura e IaC
Para utilizar el esquema PUB/SUB, se considerará la utilización de los siguientes servicios:

### 1.1 A.
 - Amazon Simple Notification Service (SNS), quien publicará los mensaje que lleguen desde endpoint
 - Amazon Simple Queue Service (SQS), quien se encargara de procesar los mensajes encolados

### 1.1 B.
Se considero una base de datos Postgres
 - En la siguiente ruta "helm-charts\postgres-citus" se encuentran los helm-chart para montar la base de datos en kubernetes
 - En la siguiente ruta "terraform\db_postgres" se encuentran los código terraform para levantar una base de datos con el servicio de RDS de AWS.

### 1.1 C.
Se crearon 2 endpoint usando FastApi con Python
 - POST : {{URI}}/ingresar-datos -> 
 - GET  : {{URI}}/data/{{ID_REGISTRO}}

## 1.2 
Con la ayuda de terraform se crearon los script para la creación de los recursos necesarios
 - Base de datos Postgres SQL -> terraform\db_postgres\main.tf
 - Cluster Kubernetes con AWS -> terraform\cluster_kubernetes\main.tf
 - Amazon Simple Notification Service (SNS) -> terraform\SNS\main.tf
 - Amazon Simple Queue Service (SQS) -> terraform\SQS\main.tf
 - Lambda para montar SQS -> terraform\lambda\main.tf



# Parte 2 - Aplicaciones y flujo CI/CD
  - 2.1 Se crea microservicio llamado "latam_api_sns_publisher" el cual se encarga publicar mensaje en servicio SNS de forma asincronica con la funcion python "start_publishing_endpoint", de igual forma levanta 2 ENDPOINT:
     * POST
     Para utilizar este ENDPOINT se debe realizar bajo la siguiente URL "{{URI}}/ingresar-datos"


     

     * GET
  - 2.2
  - 2.3
  - 2.4



