from sqlalchemy import Column, Integer, String, Boolean, ForeignKey     # noqa
from sqlalchemy.orm import relationship                                 # noqa

from app.db.base_class import Base


class ToDoEntry(Base):
    """
    Model representing a single entry in a to-do list

    Relations:
        - Has a foreign key to ToDoList, establishing a one-to-many
            relationship b/t list -> entries
    """
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    key = Column(String(256), unique=True, index=True)
    is_complete = Column(Boolean, default=False)
    # todolist_id = Column(Integer, ForeignKey("todolist.id"))
    # todolist = relationship("ToDoList", back_populates="entries")
