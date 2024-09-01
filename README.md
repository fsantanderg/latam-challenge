# latam-challenge

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
     * POST:
       Para utilizar este ENDPOINT se debe realizar bajo la siguiente URL "{{URI}}/ingresar-datos".
       
       Información para los headers: 
        - Key: Content-Type
        - Value: application/json
       
       En body se debe enviar en formato json como el siguiente ejemplo:
        {
            "topic_arn": "data-ingestion-topic",
            "message": "Este es un mensaje de prueba para el Challenge Latam."
        }

        El ENDPOINT debera devolver con un OK e indicar el transaction_id
       ![ENDPOINT POST](static/post.png)

     * GET
       Para utilizar este ENDPOINT se debe realizar bajo la siguiente URL {{URI}}/data/{{ID_REGISTRO}}
       donde se debera reemplazar la variable "{{ID_REGISTRO}}" por el ID del registro a consultar
       
  - 2.2 Para el proceso CI/CD se recomienda el uso de Jenkins para CI y ArgoCD para el proceso de CD
        - Archivo Dockerfile para crear imagen de API HTTP en ruta "ingreso-datos\publicador\Dockerfile"
        - Archivo Docker para el procesamiento de la información encolada en servicio SQS en ruta "ingreso-datos\suscriptor\Dockerfile"
        - Para el proceso CD de MS API HTTP llamado ""latam_api_sns_publisher"" se utilizo Helm-Charts template el cual se encuentra OK para ser integrado facilmente con ArgoCD
        - Se debera ingresar a la ruta donde se encuentra archivo values.yaml e ingresar el siguiente comando para regenerar archivo principal output.yaml "helm template app-api-publisher ./ > output.yaml"
        - Finalmente aplicar archivo manifiesto .yaml con el siguiente comando "kubectl apply -f output.yaml"
  
  - 2.3 Código de implementación para que el sistema pueda suscribirse se encuentra funcional y de forma asincronica permitiendo asi cargas altas de consultas
  - 2.4 Lamentablemente, no he podido realizar el diagrama con algún software para mejorar su creación, se adjunta diagrama realizado a mano "diagrama.pdf"

# Parte 3 - Pruebas de integración
 - 3.1 Se considero la creación de test unitarios simples y basicos para cubrir el requerimientos utilizando pytest, ruta "test\test_api.py"
 - 3.2 Para realizar otras pruebas que tengan mayor fidelidad, se recomiendan test sinteticos, se podria utilizar la app de "https://app.getanteon.com/" en este servicio es posible validar con diferentes tipos de carga carga: Lineal, incremental y en forma de ola (pikcs), aqui un ejemplo del como se podria implementar "test\synthetic_tests.py". De igual forma es recomendable un servicio monitoring fuera de la infraestructura propia como lo es Datadog, con ello tener la seguridad de siempre tener el control de la infraestructura en tiempo real. 
 - 3.3 Se recomienda validar los permisos y privilegios asociados de las services account de los microservicios.
 - 3.4 Para robusteser la infraestructura es fundamental identificar las áreas de vulnerabilidad o posibles fallas en el sistema y luego implementar estrategias que mitiguen esos riesgos:
    _ Monitoreo y Alertas Proactivas: Implementar herramientas de monitoreo en tiempo real y configurar alertas automáticas para detectar y responder rápidamente a anomalías.
    _ Redundancia y Alta Disponibilidad: Asegurar la redundancia en componentes críticos, implementar clustering y configurar failover automatizado para mantener el sistema operativo incluso en caso de fallos.
    _ Escalabilidad Automática: Configurar autoscaling y balanceadores de carga para manejar automáticamente aumentos en la demanda y evitar sobrecargas, configuración del Horizontal Pod Autoscaller y/o Vertical Pod Autoscaller, este último se recomiendas para servicios transaccionales.
    _ Evaluación Continua y Mejora: Realizar revisiones periódicas de la arquitectura y adoptar nuevas tecnologías para mejorar la robustez y eficiencia del sistema, como por ejemplo Blue-Green el cual su despliegue consiste en tener dos entornos de producción (Blue y Green) donde el % de propagación del nuevo release es posible controlarlo, aparte de mover el trafico rapidamente al ambiente Blue en caso de tener algún error internamente en ambiente Blue.

# Parte 4 - Métricas y Monitoreo
 - 4.1 
 - 4.2
 - 4.3
 - 4.4
 - 4.5


