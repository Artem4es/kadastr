from celery.result import AsyncResult
from fastapi import APIRouter, Request

from kadastr.schemas import QueryGet, QueryResp, ResultCheckStatus, ResultResp
from tasks.tasks import celery, get_response
from tasks.utils import check_task_exists

router = APIRouter()


@router.post('/query', response_model=QueryResp)
async def query(
    data: QueryGet,
):
    task_id = get_response.delay(dict(data)).id
    print(task_id)
    return {"query_id": f"{task_id}"}


@router.post('/result', response_model=ResultResp)
async def result(data: ResultCheckStatus):
    # print(data.query_id)
    if check_task_exists(data.query_id):
        task = AsyncResult(id=str(data.query_id), app=celery)
        # response = task.get()

        status = task.status
        if task.status == 'SUCCESS':
            return task.result
        return {'result': status}
    return {'result': 'this query_id doesn\'t exist'}


@router.get('/ping')
async def ping():
    return {'server_status': 'ok'}
