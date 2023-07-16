import os

from dotenv import load_dotenv

env = load_dotenv()

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
