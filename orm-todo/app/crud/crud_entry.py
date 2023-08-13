from app.crud.base import CRUDBase
from app.models.ToDoEntry import ToDoEntry
from app.schemas.todo_entry import TodoEntryCreate, TodoEntryUpdate


class CRUDToDoEntry(CRUDBase[ToDoEntry, TodoEntryCreate, TodoEntryUpdate]):
    pass


todo_entry = CRUDToDoEntry(ToDoEntry)
