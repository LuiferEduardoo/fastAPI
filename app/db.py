from sqlmodel import SQLModel, create_engine
from pydantic_settings import BaseSettings


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


def init_db():
    SQLModel.metadata.create_all(engine)
