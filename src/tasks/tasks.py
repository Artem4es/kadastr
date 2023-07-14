import time
from random import getrandbits

from celery import Celery
from httpx import Client

from src.config import EXTERNAL_API, REDIS_HOST, REDIS_PORT

celery = Celery(
    'tasks',
    backend=f'redis://{REDIS_HOST}:{REDIS_PORT}',
    broker=f'redis://{REDIS_HOST}:{REDIS_PORT}',
)


@celery.task  # (bind=True)
def get_response(data):
    response = {"result": bool(getrandbits(1))}
    with Client(base_url=EXTERNAL_API) as client:  # нужен асинхронный?
        # response = client.get('/result')
        # response = response.json()
        time.sleep(30)  # 60
    return response
