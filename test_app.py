import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_get_item_found(client):
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert data["name"] == "Widget A"
    assert data["price"] == 9.99


def test_get_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Item not found"
