from app.crud.base import CRUDBase
from app.models.ToDoEntry import ToDoEntry

"""
Concrete instantiation of the base class,
overrides to CRUD methods specific to ToDoEntry would go here.

Object is imported in __init__.py and passed around from there.
"""

todo_entry = CRUDBase(ToDoEntry)
