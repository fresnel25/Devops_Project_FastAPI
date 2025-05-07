from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_item():
    response = client.post(
        "/api/createitem",
        json={
            "name": "TestItem",
            "price": 99.99,
            "quantity": 5,
            "in_stock": True
        },
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "message" in response.json()


def test_get_all_items():
    response = client.get("/api/getallitems")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert isinstance(response.json()["data"], list)


def test_get_single_item():
    # D'abord créer l'item
    client.post(
        "/api/createitem",
        json={
            "name": "SingleItem",
            "price": 15.0,
            "quantity": 3,
            "in_stock": False
        },
    )
    # Ensuite le récupérer
    response_all = client.get("/api/getallitems")
    last_item = response_all.json()["data"][-1]
    item_id = last_item["id"]

    response = client.get(f"/api/getitem/{item_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["data"]["id"] == item_id


def test_update_item():
    # Créer un item à mettre à jour
    client.post(
        "/api/createitem",
        json={
            "name": "UpdateMe",
            "price": 25.0,
            "quantity": 1,
            "in_stock": True
        },
    )
    response_all = client.get("/api/getallitems")
    item_id = response_all.json()["data"][-1]["id"]

    # Mettre à jour l'item
    response = client.put(
        f"/api/edititem/{item_id}",
        json={
            "name": "UpdatedItem",
            "price": 30.0,
            "quantity": 2,
            "in_stock": False
        },
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Item updated successfully"


def test_delete_item():
    # Créer un item à supprimer
    client.post(
        "/api/createitem",
        json={
            "name": "DeleteMe",
            "price": 5.0,
            "quantity": 1,
            "in_stock": False
        },
    )
    response_all = client.get("/api/getallitems")
    item_id = response_all.json()["data"][-1]["id"]

    # Supprimer l'item
    response = client.delete(f"/api/deleteitem/{item_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Item deleted successfully"

    # Vérifier qu’il a bien été supprimé
    response = client.get(f"/api/getitem/{item_id}")
    assert response.status_code == 200
    assert response.json()["success"] is False
