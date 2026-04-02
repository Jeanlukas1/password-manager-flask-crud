import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

passwords_list = []

def test_create_password():
    payload = {
    "name": "Password Teste",
    "password": "PasswordTeste@"
    }
    response = requests.post(f"{BASE_URL}/passwords", json=payload)
    assert response.status_code == 200
    
    response_json = response.json()
    assert "name" in response_json