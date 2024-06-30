import os
import sys
from typing import List
from typing import Optional
from typing import Union

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings

from loguru import logger
from utils.camel_model import to_camel as camel_string


class Settings(BaseSettings):
    HOST: str = "localhost"

    # API
    PROJECT_NAME: str

    DEFAULT_LANGUAGE: Optional[str] = "pl"

    API_PORT: str
    API_ROOT_PATH: str = "/api"

    # RabbitMQ
    RABBITMQ_IN_WEBSOCKET_HOST_NAME: str
    RABBITMQ_IN_WEBSOCKET_USERNAME: str
    RABBITMQ_IN_WEBSOCKET_PASSWORD: str
    RABBITMQ_IN_WEBSOCKET_PORT: int

    # e.g: '["http://localhost","http://localhost:4200","http://localhost:3000"]'
    CORS_ORIGINS: List[AnyHttpUrl] = []

settings = Settings(_env_file=".env", _env_file_encoding="utf-8") if os.path.exists(".env") else Settings()
