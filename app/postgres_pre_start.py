from app.models.ToDoEntry import ToDoEntry  # noqa
from app.models.User import User            # noqa
from app.db.session import engine
from app.db.base_class import Base


def init_db():
    print("Creating all tables in the database...")
    Base.metadata.create_all(bind=engine)
