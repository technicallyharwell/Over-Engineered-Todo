import pytest

from app.crud.user import CRUDUser
from app.models.User import User

from tests.config.stubbed_user_entries import USER_TESTING_ENTRIES


@pytest.fixture(scope="function")
def crud_user() -> CRUDUser:
    return CRUDUser(User)


@pytest.fixture(scope="function", autouse=True)
def setup_db(db_session):
    """
    Fixture to set up the db with some test data
    """
    for entry in USER_TESTING_ENTRIES:
        db_obj = User(**entry)
        db_session.add(db_obj)
    db_session.commit()
    yield
    db_session.query(User).delete()
    db_session.commit()


def test_get(crud_user, db_session):
    user = crud_user.get(db_session, "test_user_1")
    assert user.username == "test_user_1" and user.id == 1


def test_create(crud_user, db_session):
    new_user = {"username": "test_user_300", "password": "test_password_300"}
    user = crud_user.create(db_session, obj_in=new_user)
    assert user.username == "test_user_300" and user.id is not None
