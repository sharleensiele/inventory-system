import pytest
from app.app import app 

@pytest.fixture
def client():
    return app.test_client()

def test_get_inventory(client):
    response = client.get('/inventory')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_item(client):
    response = client.post('/inventory', json={
        "name": "Test Item",
        "brand": "Test Brand",
        "price": 100,
        "stock": 10
    })
    assert response.status_code == 201
    assert response.json["name"] == "Test Item"

def test_update_item(client):
    # Ensure item exists
    client.post('/inventory', json={
        "name": "Update Item",
        "brand": "Brand",
        "price": 50,
        "stock": 5
    })
    response = client.patch('/inventory/1', json={"price": 500})
    assert response.status_code == 200
    assert response.json["price"] == 500

def test_delete_item(client):
    # Ensure item exists
    client.post('/inventory', json={
        "name": "Delete Item",
        "brand": "Brand",
        "price": 50,
        "stock": 5
    })
    response = client.delete('/inventory/1')
    assert response.status_code == 200
    assert response.json["message"] == "Item deleted"