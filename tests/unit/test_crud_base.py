import pytest

from app.crud.base import CRUDBase
from app.models.ToDoEntry import ToDoEntry

from tests.config.stubbed_db_entries import TODO_TESTING_ENTRIES


@pytest.fixture(scope="function")
def crud_base() -> CRUDBase:
    return CRUDBase(ToDoEntry)


@pytest.fixture(scope="function", autouse=True)
def setup_db(db_session):
    """
    Fixture to set up the db with some test data
    """
    for entry in TODO_TESTING_ENTRIES:
        db_obj = ToDoEntry(**entry)
        db_session.add(db_obj)
    db_session.commit()
    yield
    db_session.query(ToDoEntry).delete()
    db_session.commit()


def test_get(crud_base, db_session):
    entry = crud_base.get(db_session, id=100)
    assert entry.key == "test100" and entry.id == 100


def test_get_multi(crud_base, db_session):
    entries = crud_base.get_multi(db_session)
    assert isinstance(entries, list)


def test_create(crud_base, db_session):
    new_entry = {"id": 300, "key": "test300", "is_complete": False}
    entry = crud_base.create(db_session, obj_in=new_entry)
    assert entry.key == "test300" and entry.id == 300


def test_update(crud_base, db_session):
    original_entry = crud_base.get(db_session, id=100)
    updated_entry = crud_base.update(db_session,
                                     db_obj=original_entry,
                                     obj_in={"is_complete": True})
    assert updated_entry.is_complete is True


def test_remove(crud_base, db_session):
    entry = crud_base.get(db_session, id=200)
    crud_base.remove(db_session, id=entry.id)
    assert crud_base.get(db_session, id=200) is None
