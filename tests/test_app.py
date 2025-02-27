import pytest
from src.app import app
import sys
import os

# Add src/ to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app  # Now it should work!


@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, CI/CD!"
