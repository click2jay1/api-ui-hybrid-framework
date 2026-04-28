import json

import pytest
from utils.api_client import APIClient

@pytest.fixture
def api():
    return APIClient()

def test_create_user_successfully(api):
    response = api.create_user("John Doe", "QA Lead")
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    print("\nResponse code", response.status_code)
    print("\nResponse Body: \n", json.dumps(response.json(), indent=2))

    user_id = response.json()["id"]
    response = api.get_user(user_id)
    '''This is a dummy portal for testing pupose, 
    so the user gets deleted as soon as it is created, so expect empty response
    '''
    print("New User:\n", response.json())
