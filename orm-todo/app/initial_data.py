import logging

from app.db.base import Base
from app.db.init_db import init_db
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


"""
INFO:__main__:When initializing mapper mapped class 
ToDoEntry->todoentry, expression 'ToDoList' failed to locate a name ('ToDoList'). 
If this is a class name, consider adding this relationship() to the <class 'app.models.ToDoEntry.ToDoEntry'> 
class after both dependent classes have been defined.
"""

def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.info(e)
        import time
        time.sleep(50)
