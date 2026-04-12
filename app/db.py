from sqlmodel import SQLModel, create_engine, Session
from pydantic_settings import BaseSettings
from fastapi import Depends
from typing import Annotated
from contextlib import asynccontextmanager


class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 3306
    db_user: str = "fastapi_user"
    db_password: str = "fastapi_pass"
    db_name: str = "platzi_fastapi"

    class Config:
        env_file = ".env"


settings = Settings()

DATABASE_URL = f"mysql+pymysql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


@asynccontextmanager
async def init_db():
    SQLModel.metadata.create_all(engine)
    yield


SessionDep = Annotated[Session, Depends(get_session)]

# Importar modelos para registrar en metadata
from app.models import Customer, Transaction, Invoice
