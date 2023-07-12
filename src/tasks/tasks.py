import time
from random import getrandbits

from celery import Celery
from httpx import Client

celery = Celery(
    'tasks', backend='redis://localhost:6379', broker='redis://localhost:6379'
)
external_url = 'https://example.com'


@celery.task  # (bind=True)
def get_response(data):
    response = {"result": bool(getrandbits(1))}
    with Client() as client:  # нужен асинхронный?
        # response = client.post(external_url, data=data)
        time.sleep(30)  # 60
    return response  # рандом
