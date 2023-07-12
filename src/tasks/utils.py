from kombu.exceptions import OperationalError

from tasks.tasks import celery


def check_task_exists(uuid):
    try:
        with celery.connection() as connection:  # возвращает False для обрбатывамой функции!!!
            exists = connection.default_channel.client.exists(
                f'celery-task-meta-{uuid}'
            )
            return exists
    except OperationalError:
        # Обработка ошибки подключения к Redis
        raise OperationalError('Custom error, while trying to check uuid')
