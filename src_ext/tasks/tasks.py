from random import getrandbits, randrange
from time import sleep

from celery import Celery

from src_ext.external_api import config

celery = Celery(
    'tasks',
    backend=f'redis://{config.REDIS_HOST}:{config.REDIS_PORT}',
    broker=f'redis://{config.REDIS_HOST}:{config.REDIS_PORT}',
)


@celery.task
def process_data(data):
    """Sends data to ext API and recieves UUID for tracking"""
    response = {"result": bool(getrandbits(1))}
    sleep(randrange(0, 60))
    return response
