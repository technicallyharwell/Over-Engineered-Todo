from app.crud.base import CRUDBase


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "entries" in response.json()


def test_get_entry(client, monkeypatch):
    test_entry = {"id": 1, "key": "first", "is_complete": False}

    def mock_get(*args, **kwargs):
        return test_entry

    # CRUDBase get method is mocked so that the database is not written to for testing
    monkeypatch.setattr(CRUDBase, "get", mock_get)

    response = client.get("/entry/first")
    assert response.status_code == 200
    assert response.json()["key"] == "first"


def test_get_entry_not_found(client, monkeypatch):
    def mock_get(*args, **kwargs):
        return None

    # CRUDBase get method is mocked so that the database is not written to for testing
    monkeypatch.setattr(CRUDBase, "get", mock_get)

    response = client.get("/entry/first")
    assert response.status_code == 404


def test_create_entry(client):
    test_entry = {"id": 1, "key": "first", "is_complete": False}

    response = client.post("/entry", json=test_entry)
    assert response.status_code == 201
    assert response.json()["key"] == "first"


def test_update_entry(client):
    test_entry = {"id": 1, "key": "first", "is_complete": False}
    client.post("/entry", json=test_entry)

    update_entry = {"id": 1, "key": "first", "is_complete": True}

    response = client.put("/entry", json=update_entry)
    assert response.status_code == 200
    assert response.json()["is_complete"] is True


def test_update_entry_not_found(client):
    update_entry = {"id": 1, "key": "first", "is_complete": True}

    response = client.put("/entry", json=update_entry)
    assert response.status_code == 404


def test_delete_entry(client):
    test_entry = {"id": 1, "key": "first", "is_complete": False}
    client.post("/entry", json=test_entry)

    response = client.delete("/entry/first")
    assert response.status_code == 200
    assert response.json()["key"] == "first"


def test_delete_entry_not_found(client):
    response = client.delete("/entry/non_existent_entry")
    assert response.status_code == 404
