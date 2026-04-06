import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

def test_create_password():
    payload = {
    "name": "Password Teste",
    "password": "PasswordTeste@"
    }
    response = requests.post(f"{BASE_URL}/passwords", json=payload)
    assert response.status_code == 200
    
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    
def test_list_password():
    payload = {
    "name": "Password Teste 2",
    "password": "PasswordTeste@ 2"
    }
    response = requests.post(f"{BASE_URL}/passwords", json=payload)
    assert response.status_code == 200
    
    create_response = response.json()

    response = requests.get(f"{BASE_URL}/passwords")
    assert response.status_code == 200
    
    response_json = response.json()
    
    ids = [item["id"] for item in response_json]
    
    assert create_response["id"] in ids
    
    assert isinstance(response_json, list)
    assert "id" in response_json[0]
    assert "name" in response_json[0]
    
def test_update_password():
    # 1. Criar uma senha
    payload = {
        "name": "Teste",
        "password": "123"
    }

    create = requests.post(f"{BASE_URL}/passwords", json=payload)
    assert create.status_code == 200

    created = create.json()
    password_id = created["id"]

    # 2. Atualizar a senha
    update_payload = {
        "name": "Teste Atualizado",
        "password": "456"
    }

    response = requests.put(
        f"{BASE_URL}/passwords/{password_id}",
        json=update_payload
    )

    # 3. Validações
    assert response.status_code == 200
    assert "updated" in response.json()["message"]
    
def test_delete_password():
    # 1. Criar uma senha
    payload = {
        "name": "Teste Delete",
        "password": "123"
    }

    create = requests.post(f"{BASE_URL}/passwords", json=payload)
    assert create.status_code == 200

    created = create.json()
    password_id = created["id"]

    # 2. Deletar a senha
    response = requests.delete(f"{BASE_URL}/passwords/{password_id}")

    # 3. Validações
    assert response.status_code == 200
    assert "deleted" in response.json()["message"]

    # 4. Garantir que foi removido
    get_all = requests.get(f"{BASE_URL}/passwords")

    if get_all.status_code == 200:
        data = get_all.json()
        ids = [item["id"] for item in data]

        assert password_id not in ids