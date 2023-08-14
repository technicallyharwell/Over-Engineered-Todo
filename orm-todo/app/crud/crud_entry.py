from typing import Dict, Union, Any

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.ToDoEntry import ToDoEntry
from app.schemas.todo_entry import TodoEntryCreate, TodoEntryUpdate


class CRUDToDoEntry(CRUDBase[ToDoEntry, TodoEntryCreate, TodoEntryUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: ToDoEntry,
        obj_in: Union[TodoEntryUpdate, Dict[str, Any]]
    ) -> ToDoEntry:

        updated_obj = db_obj
        updated_obj.is_complete = obj_in.is_complete

        db.add(updated_obj)
        db.commit()
        db.refresh(updated_obj)
        return updated_obj


todo_entry = CRUDToDoEntry(ToDoEntry)
