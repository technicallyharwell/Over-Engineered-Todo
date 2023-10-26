from sqlalchemy import Column, Integer, String, Boolean, ForeignKey     # noqa
from sqlalchemy.orm import relationship                                 # noqa

from app.db.base_class import Base


class User(Base):
    """
    SQLAlchemy model representing a single user in the system
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(256), unique=True, index=True)
    hashed_password = Column(String(256))
    is_active = Column(Boolean, default=True)
    # lists = relationship("ToDoList", back_populates="owner")
