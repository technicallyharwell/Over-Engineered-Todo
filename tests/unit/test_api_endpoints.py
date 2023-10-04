from app.crud.base import CRUDBase
from app.crud.crud_entry import CRUDToDoEntry


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

    response = client.get("/entry/1")
    assert response.status_code == 200
    assert response.json()["key"] == "first"


def test_get_entry_not_found(client, monkeypatch):
    def mock_get(*args, **kwargs):
        return None

    # CRUDBase get method is mocked so that the database is not written to for testing
    monkeypatch.setattr(CRUDBase, "get", mock_get)

    response = client.get("/entry/1")
    assert response.status_code == 404


def test_create_entry(client, monkeypatch):
    test_entry = {"id": 1, "key": "create", "is_complete": False}

    def mock_post(*args, **kwargs):
        return test_entry

    # CRUDBase create method is mocked so that the database is not written to for testing
    monkeypatch.setattr(CRUDBase, "create", mock_post)

    response = client.post("/entry", json=test_entry)
    assert response.status_code == 201
    assert response.json()["key"] == "create"


def test_update_entry(client, monkeypatch):
    test_entry = {"id": 1, "key": "update", "is_complete": False}
    update_entry = {"id": 1, "key": "update", "is_complete": True}

    def mock_create(*args, **kwargs):
        return test_entry

    def mock_update(*args, **kwargs):
        updated_entry = kwargs["obj_in"]
        updated_field = updated_entry.is_complete
        test_entry["is_complete"] = updated_field
        return test_entry

    # CRUDBase get method is mocked so that update thinks the entry exists
    monkeypatch.setattr(CRUDBase, "get", mock_create)

    # CRUDToDoEntry update method is mocked so that the database is not written to for testing
    monkeypatch.setattr(CRUDToDoEntry, "update", mock_update)

    response = client.put("/entry", json=update_entry)
    assert response.status_code == 200
    assert response.json()["is_complete"] is True


def test_update_entry_not_found(client):
    update_entry = {"id": 1, "key": "first", "is_complete": True}

    response = client.put("/entry", json=update_entry)
    assert response.status_code == 404


def test_delete_entry(client, monkeypatch):
    test_entry = {"id": 1, "key": "delete", "is_complete": False}

    def mock_get(*args, **kwargs):
        from app.models.ToDoEntry import ToDoEntry
        return ToDoEntry(**test_entry)

    def mock_delete(*args, **kwargs):
        return test_entry

    # CRUDBase get method is mocked so that delete thinks the entry exists
    monkeypatch.setattr(CRUDBase, "get", mock_get)

    # CRUDBase delete method is mocked so that the database is not written to for testing
    monkeypatch.setattr(CRUDBase, "remove", mock_delete)

    response = client.delete("/entry/1")
    assert response.status_code == 200
    assert response.json()["key"] == "delete"


def test_delete_entry_not_found(client):
    response = client.delete("/entry/1")
    assert response.status_code == 404
