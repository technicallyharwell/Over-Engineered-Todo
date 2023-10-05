from app.crud.base import CRUDBase
from app.crud.crud_entry import CRUDToDoEntry


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "entries" in response.json()


def test_get_entry(client, monkeypatch):
    test_entry = {"id": 1, "entry": "first", "is_complete": False}

    def mock_get(*args, **kwargs):
        return test_entry

    # CRUDBase get method is mocked so that the database is not written to for testing
    monkeypatch.setattr(CRUDBase, "get", mock_get)

    response = client.get("/entries/1")
    print(f"response: {response.json()}")
    assert response.status_code == 200
    assert response.json()["entry"] == "first"


def test_get_entry_not_found(client, monkeypatch):
    def mock_get(*args, **kwargs):
        return None

    # CRUDBase get method is mocked so that the database is not written to for testing
    monkeypatch.setattr(CRUDBase, "get", mock_get)

    response = client.get("/entries/1")
    assert response.status_code == 404


def test_create_entry(client, monkeypatch):
    test_entry = {"id": 1, "entry": "create", "is_complete": False}

    def mock_post(*args, **kwargs):
        return test_entry

    # CRUDBase create is mocked so that the database is not written to
    monkeypatch.setattr(CRUDBase, "create", mock_post)

    response = client.post("/entries", json=test_entry)
    assert response.status_code == 201
    assert response.json()["entry"] == "create"


def test_update_entry(client, monkeypatch):
    test_entry = {"id": 1, "entry": "update", "is_complete": False}
    update_entry = {"id": 1, "entry": "update", "is_complete": True}

    def mock_create(*args, **kwargs):
        return test_entry

    def mock_update(*args, **kwargs):
        updated_entry = kwargs["obj_in"]
        updated_field = updated_entry.is_complete
        test_entry["is_complete"] = updated_field
        return test_entry

    # CRUDBase get method is mocked so that update thinks the entry exists
    monkeypatch.setattr(CRUDBase, "get", mock_create)

    # CRUDToDoEntry update is mocked so that the database is not written to
    monkeypatch.setattr(CRUDToDoEntry, "update", mock_update)

    response = client.put("/entries", json=update_entry)
    assert response.status_code == 200
    assert response.json()["is_complete"] is True


def test_update_entry_not_found(client):
    update_entry = {"id": 1, "entry": "first", "is_complete": True}

    response = client.put("/entries", json=update_entry)
    assert response.status_code == 404


def test_delete_entry(client, monkeypatch):
    test_entry = {"id": 1, "entry": "delete", "is_complete": False}

    def mock_get(*args, **kwargs):
        from app.models.ToDoEntry import ToDoEntry
        return ToDoEntry(**test_entry)

    def mock_delete(*args, **kwargs):
        return test_entry

    # CRUDBase get method is mocked so that delete thinks the entry exists
    monkeypatch.setattr(CRUDBase, "get", mock_get)

    # CRUDBase delete method is mocked so that the database is not written to
    monkeypatch.setattr(CRUDBase, "remove", mock_delete)

    response = client.delete("/entries/1")
    assert response.status_code == 200
    assert response.json()["entry"] == "delete"


def test_delete_entry_not_found(client):
    response = client.delete("/entries/1")
    assert response.status_code == 404
