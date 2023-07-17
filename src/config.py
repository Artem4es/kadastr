import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

env = load_dotenv()


class Config(BaseSettings):
    EXTERNAL_API: str = os.environ.get("EXTERNAL_API")
    REDIS_HOST: str = os.environ.get("REDIS_HOST")
    REDIS_PORT: str = os.environ.get("REDIS_PORT")
    DEBUG: bool = os.environ.get("DEBUG")
    API_NAME: str = os.environ.get("API_NAME")
