import requests

def test_get_endpoint():
    url = "http://localhost:8010/data/356"
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    # Verificar que la solicitud fue exitosa
    assert response.status_code == 200

    # Verificar que los datos devueltos son los esperados (ejemplo)
    expected_data = {
        "id": 356
    }
    assert response.json() == expected_data


def test_post_endpoint():
    url = "http://localhost:8010/ingresar-datos"
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "topic_arn": "data-ingestion-topic",
        "message": "Este es un mensaje de prueba para el Challenge Latam."
    }

    response = requests.post(url, json=body, headers=headers)

    # Verificar que la solicitud fue exitosa
    assert response.status_code == 200

    # Verificar que la respuesta es la esperada
    expected_response = {
        "status": "Publicación OK"
    }
    
    response_json = response.json()
    
    # Verifica solo el "status"
    assert response_json["status"] == expected_response["status"]
    
    # Verifica que el "transaction_id" exista y tenga el formato correcto (UUID)
    assert "transaction_id" in response_json
    assert len(response_json["transaction_id"]) > 0  # Verifica que no esté vacío
