from redis import Redis

from src_ext.external_api import config

redis_client = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
)


def set_task(id):
    redis_client.rpush('tasks_started', id)


def check_task_exists(id):
    for one in redis_client.lrange("tasks_started", 0, -1):
        task_info = one.decode()
        if task_info == id:
            return True
    return False
