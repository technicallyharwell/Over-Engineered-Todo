from pydantic import BaseModel


class ToDoEntry(BaseModel):
    """
    A single entry in the todo list, represented via JSON
    """
    id: int
    is_complete: bool = False
    key: str


class ToDoList(BaseModel):
    todos: list[ToDoEntry]


class ToDoEntryCreate(BaseModel):
    key: str
