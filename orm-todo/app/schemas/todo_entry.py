from pydantic import BaseModel, ConfigDict


class TodoEntryBase(BaseModel):
    key: str


class TodoEntryCreate(TodoEntryBase):
    key: str


class TodoEntryUpdate(TodoEntryBase):
    key: str
    is_complete: bool


"""
We separate these so that in the future we can easily 
modify which props are returned to the client
"""


# Props shared by models in DB
class TodoEntryInDB(TodoEntryBase):
    id: int
    key: str
    is_complete: bool

    # the Config class approach was deprecated in favor of ConfigDict in pydantic 2.0
    model_config = ConfigDict(from_attributes=True)


# Return these props to the client
class TodoEntry(TodoEntryInDB):
    id: int
    key: str
    is_complete: bool
