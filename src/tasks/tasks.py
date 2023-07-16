from celery import Celery
from httpx import Client

from src.config import EXTERNAL_API, REDIS_HOST, REDIS_PORT

celery = Celery(
    'tasks',
    backend=f'redis://{REDIS_HOST}:{REDIS_PORT}',
    broker=f'redis://{REDIS_HOST}:{REDIS_PORT}',
)

client = Client(base_url=EXTERNAL_API)


@celery.task
def get_response(data):
    """Sends data to ext API and recieves UUID for tracking"""
    with Client(base_url=EXTERNAL_API) as client:
        response = client.post(yurl='/query', json=dict(data))  # переделать

    return response.json()
