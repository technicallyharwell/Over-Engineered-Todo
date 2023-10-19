import logging
import os
from functools import lru_cache
from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Grabbing settings from the environment")


class Settings(BaseSettings):
    if os.getenv("CONTAINERIZED", None) is None:
        logger.info("Loading local .env file")
        # env vars are not injected from a container, load the local .env file
        from dotenv import load_dotenv
        if "app" in os.getcwd():
            logger.info("Loading local .env file from app directory")
            load_dotenv("../configs/local/sqlite.env")  # running main.py
        elif "test" in os.getcwd():
            logger.info("Loading local .env file from test directory")
            load_dotenv("../../configs/local/sqlite.env")   # init conftest
        else:
            logger.info("Loading local .env file from root directory")
            load_dotenv("./configs/local/sqlite.env")   # tests execution
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
