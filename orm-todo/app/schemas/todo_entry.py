from pydantic import BaseModel
from typing import Optional


class TodoEntryBase(BaseModel):
    key: str


class TodoEntryCreate(TodoEntryBase):
    key: str


class TodoEntryUpdate(TodoEntryBase):
    key: str
    is_complete: bool


"""
We separate these so that in the future we can easily modify which props are returned to the client
"""


# Props shared by models in DB
class TodoEntryInDB(TodoEntryBase):
    id: int
    key: str
    is_complete: bool

    # Pydantic's orm_mode will tell the model to read the data even if it's not a dict
    class Config:
        orm_mode = True


# Return these props to the client
class TodoEntry(TodoEntryInDB):
    id: int
    key: str
    is_complete: bool


