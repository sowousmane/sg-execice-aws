import os
import sys

from fastapi.testclient import TestClient

from app.main import app

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))


def test_home():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
