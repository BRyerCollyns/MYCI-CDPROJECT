import pytest
from src.app import app  # Correct import

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, CI/CD!"
