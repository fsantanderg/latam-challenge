import os
import requests

ANTEON_API_KEY = os.getenv("ANTEON_API_KEY")
ANTEON_API_BASE_URL = "https://api.getanteon.com/v1"

headers = {
    "Authorization": f"Bearer {ANTEON_API_KEY}",
    "Content-Type": "application/json"
}

def create_synthetic_test(name, url, method, payload=None):
    endpoint = f"{ANTEON_API_BASE_URL}/synthetic_tests"
    steps = [
        {
            "type": method,
            "url": url,
            "headers": {
                "Content-Type": "application/json"
            }
        }
    ]

    if method == "POST" and payload:
        steps[0]["body"] = payload

    data = {
        "name": name,
        "interval": 5,  # Intervalo en minutos para ejecutar el test
        "locations": ["us-east-2"],  # Especificar la ubicación del test
        "steps": steps
    }

    response = requests.post(endpoint, json=data, headers=headers)
    response.raise_for_status()  # Lanza un error si la solicitud falla
    return response.json()

def run_synthetic_test(test_id):
    endpoint = f"{ANTEON_API_BASE_URL}/synthetic_tests/{test_id}/run"
    response = requests.post(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_test_results(test_id):
    endpoint = f"{ANTEON_API_BASE_URL}/synthetic_tests/{test_id}/results"
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

# Crear test para el endpoint GET
get_test = create_synthetic_test(
    name="GET Test for /data/275",
    url="http://localhost:8010/data/275",
    method="GET"
)
print("GET Test creado:", get_test)

# Crear test para el endpoint POST
post_test = create_synthetic_test(
    name="POST Test for /ingresar-datos",
    url="http://localhost:8010/ingresar-datos",
    method="POST",
    payload={
        "topic_arn": "data-ingestion-topic",
        "message": "Este es un mensaje de prueba para el Challenge Latam."
    }
)
print("POST Test creado:", post_test)

# Ejecutar los tests
get_test_result = run_synthetic_test(get_test['id'])
print("Resultado de la ejecución del test GET:", get_test_result)

post_test_result = run_synthetic_test(post_test['id'])
print("Resultado de la ejecución del test POST:", post_test_result)

# Obtener los resultados de los tests
get_results = get_test_results(get_test['id'])
print("Resultados del test GET:", get_results)

post_results = get_test_results(post_test['id'])
print("Resultados del test POST:", post_results)
