from fastapi import APIRouter, HTTPException, status, Depends
from jose import jwt

from app import deps
from app.config import get_settings
from app.schemas.user import UserBase


ENV_SETTINGS = get_settings()

router = APIRouter(prefix="/users", tags=["users"])


async def get_user_from_jwt_token(token: str = Depends(deps.oauth2_scheme)) -> UserBase:
    """
    Get the user from the JWT token
    """
    unauthorized_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(
            token,
            ENV_SETTINGS.jwt_hashing_secret,
            algorithms=[ENV_SETTINGS.jwt_hashing_algorithm]
        )
        username: str = payload.get("sub")
        if username is None:
            raise unauthorized_exception
        token_data = UserBase(username=username)
    except jwt.JWTError:
        raise unauthorized_exception
    return token_data


@router.get("/me", status_code=status.HTTP_200_OK, response_model=UserBase)
async def parse_user_from_token(
    user: UserBase = Depends(get_user_from_jwt_token)
) -> UserBase:
    """
    Get the user from the JWT token
    """
    return user

