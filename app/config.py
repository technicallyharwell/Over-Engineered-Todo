import logging
import os
from functools import lru_cache
from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)
logger.info("Grabbing settings from the environment")


class Settings(BaseSettings):
    if os.getenv("CONTAINERIZED", None) is None:
        logger.info("Loading local .env file")
        # env vars are not injected from a container, load the local .env file
        from dotenv import load_dotenv
        print(os.getcwd())
        if "app" in os.getcwd():
            load_dotenv("../configs/local/sqlite.env")
        elif "test" in os.getcwd():
            load_dotenv("../../configs/local/sqlite.env")
        else:
            load_dotenv("./configs/local/sqlite.env")
        db_dialect: str = os.getenv("DB_DIALECT")
    else:
        app_name: str = os.getenv("APP_NAME")
        db_user: str = os.getenv("DB_USER")
        db_password: str = os.getenv("DB_PASSWORD")
        db_name: str = os.getenv("DB_NAME")
        db_hostname: str = os.getenv("DB_HOSTNAME")
        db_port: int = os.getenv("DB_PORT")
        db_dialect: str = os.getenv("DB_DIALECT")


@lru_cache()
def get_settings() -> BaseSettings:
    logger.info("get_settings called, returning instance of Settings")
    return Settings()
