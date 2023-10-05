from pydantic import BaseModel, ConfigDict


class TodoEntryBase(BaseModel):
    pass


class TodoEntryCreate(TodoEntryBase):
    entry: str


class TodoEntryUpdate(TodoEntryBase):
    id: int
    is_complete: bool


"""
We separate these so that in the future we can easily 
modify which props are returned to the client
"""


# Props shared by models in DB
class TodoEntryInDB(TodoEntryBase):
    id: int
    entry: str
    is_complete: bool

    # the Config class approach was deprecated in favor of ConfigDict in pydantic 2.0
    model_config = ConfigDict(from_attributes=True)


# Return these props to the client
class TodoEntry(TodoEntryInDB):
    id: int
    entry: str
    is_complete: bool
