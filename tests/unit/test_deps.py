from app.deps import get_db


def test_get_db():
    db = get_db()
    assert db is not None
