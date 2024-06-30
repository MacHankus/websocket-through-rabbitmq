import time
from contextlib import contextmanager
from typing import Generator

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from core.logger import logger
from settings import settings

SQLALCHEMY_DATABASE_URL: str = (
    f"mssql+pyodbc://{settings.DB_USER}:{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?driver={settings.DB_DRIVER}"
)

engine: Engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"application_name": settings.PROJECT_NAME},
)

SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
