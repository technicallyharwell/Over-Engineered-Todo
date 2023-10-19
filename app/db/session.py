from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_settings

settings = get_settings()


def get_db_uri():
    if settings.db_dialect == "sqlite":
        return f"{settings.db_dialect}:///./test.db"
    return (f"{settings.db_dialect}://{settings.db_user}:{settings.db_password}@"
            f"{settings.db_hostname}:{settings.db_port}/{settings.db_name}")

# SQLALCHEMY_DATABASE_URI = "sqlite:///./test.db"
# POSTGRES_DATABASE_URI = "postgresql://postgres:postgres@db:5432/crud_db"


engine = create_engine(
    get_db_uri(),
    echo=True  # Log SQL queries to stdout

    # below for SQLite
    # SQLALCHEMY_DATABASE_URI,
    # FastAPI can access the DB with multiple threads in a single request,
    # ...so SQLite needs this flag
    # connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine)
