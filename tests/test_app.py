from app.app import app
import json
import pytest


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    res = client.get("/")
    assert res.status_code == 200


def test_get_inventory(client):
    res = client.get("/inventory")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)