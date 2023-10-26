from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app import deps
from app.config import get_settings
from app.crud.user import user_entry
from app.schemas.user import UserCreate, UserPost
from app.schemas.jwt_token import Token

ENV_SETTINGS = get_settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()


def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt and a random salt
    """
    return pwd_context.hash(password)


def create_access_token(
    data: dict, expires_delta: timedelta
) -> str:
    """
    Create a JWT token with the provided data and expiration time
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        ENV_SETTINGS.jwt_hashing_secret,
        algorithm=ENV_SETTINGS.jwt_hashing_algorithm
    )
    return encoded_jwt


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=dict)
def create_user(
    *,
    entry_in: UserPost,
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new user
    """
    user = user_entry.get(db=db, username=entry_in.username)
    if user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = hash_password(entry_in.password)
    create_obj = UserCreate(username=entry_in.username, hashed_password=hashed_password)
    user = user_entry.create(db=db, obj_in=create_obj)
    return {"new_user_created": user.username}


@router.post("/token", response_model=Token)
def create_new_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new JWT token for the user
    """
    user = user_entry.get(db=db, username=form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ENV_SETTINGS.jwt_expiration_time)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
