from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URI = "sqlite:///./test.db"
POSTGRES_DATABASE_URI = "postgresql://postgres:postgres@db:5432/crud_db"

engine = create_engine(
    POSTGRES_DATABASE_URI,
    echo=True  # Log SQL queries to stdout

    # below for SQLite
    # SQLALCHEMY_DATABASE_URI,
    # FastAPI can access the DB with multiple threads in a single request,
    # ...so SQLite needs this flag
    # connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine)
