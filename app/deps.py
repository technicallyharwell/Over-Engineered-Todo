from typing import Generator

from fastapi.security import OAuth2PasswordBearer

from app.db.session import SessionLocal


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
