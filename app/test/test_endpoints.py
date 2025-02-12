from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_get_address_info():
    response = client.post(
        "/address/", json={"address": "TMY19SeunpGTRoxB1yCF1EBeZjcGNy3333"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "bandwidth" in data
    assert "energy" in data
    assert "balance" in data


def test_read_logs():
    response = client.get("/logs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
