from sqlalchemy import Column, Integer, String, Boolean, DateTime  # noqa
from sqlalchemy.orm import relationship                            # noqa
from sqlalchemy.sql import func

from app.db.base_class import Base


class User(Base):
    """
    SQLAlchemy model representing a single user in the system
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(256), unique=True, index=True)
    hashed_password = Column(String(256), nullable=False)
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=func.now())
    # lists = relationship("ToDoList", back_populates="owner")
