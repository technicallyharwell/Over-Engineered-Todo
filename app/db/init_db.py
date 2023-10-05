import logging
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import base  # noqa: F401
from app.helpers.todo_entry_data import TODO_ENTRIES

logger = logging.getLogger(__name__)


def init_db(db: Session) -> None:
    """
    Initialize the database with the initial data.
    NOTE: tables should already be created with alembic_old migrations
    :param db:
    :return:
    """
    for entry in TODO_ENTRIES:
        entry_in = schemas.TodoEntryCreate(
            id=entry["id"],
            entry=entry["key"],
            is_complete=entry["is_complete"]
        )
        logger.info(f"Creating todo entry {entry_in}")
        crud.todo_entry.create(db, obj_in=entry_in)
        logger.info(f"Created todo entry with text {entry['entry']}")
