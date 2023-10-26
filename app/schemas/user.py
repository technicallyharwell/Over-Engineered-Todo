from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    """
    Base pydantic model for an individual user
    """
    username: str


class UserCreate(UserBase):
    """
    Pydantic model representing a user creation request
    """
    hashed_password: str


class UserPost(UserBase):
    """
    Pydantic model receiving a user POST request
    """
    password: str


class UserUpdate(UserBase):
    """
    Pydantic model representing a user update request
    """
    password: str


class UserInDB(UserBase):
    """
    Pydantic model representing a user in the database
    """
    id: int
    hashed_password: str
    is_active: bool
    # lists = relationship("ToDoList", back_populates="owner")

    model_config = ConfigDict(from_attributes=True)
