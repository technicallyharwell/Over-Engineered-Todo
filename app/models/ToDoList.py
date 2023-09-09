# from sqlalchemy import Column, Integer
# from sqlalchemy.orm import relationship
#
# from app.db.base_class import Base


# class ToDoList(Base):
#     """
#     Model for representing a to-do list with 0 or many entries
#
#     Relations:
#         - Has a one-to-many relationship with ToDoEntry
#     """
#     id = Column(Integer, primary_key=True, index=True)
#     entries = relationship(
#         "ToDoEntry",
#         cascade="all, delete-orphan",
#         back_populates="todolist",
#         uselist=True,)
