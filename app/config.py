from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    CORS_ORIGINS: List[str] = []

    model_config = SettingsConfigDict(env_file=".env", env_prefix="")

    # validator runs BEFORE type coercion
    @field_validator("CORS_ORIGINS", mode="before")
    def split_cors(cls, v):
        if isinstance(v, str):
            return [x.strip() for x in v.split(",") if x.strip()]
        return v

settings = Settings()
