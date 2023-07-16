from celery.result import AsyncResult
from external_api.responses import query_resp
from external_api.schemas import (
    PingResp,
    QueryGet,
    QueryResp,
    ResultCheckStatus,
    ResultResp,
)
from fastapi import APIRouter, Response, status
from tasks.tasks import celery, process_data
from tasks.utils import check_task_exists, set_task

router = APIRouter()


@router.post('/query', response_model=QueryResp)
async def query(data: QueryGet):
    """Makes query and returns query_id"""
    task_id = process_data.delay(dict(data)).id
    set_task(str(task_id))
    return {"query_id": f"{task_id}"}


@router.post('/result', response_model=ResultResp, responses=query_resp)
async def result(data: ResultCheckStatus, response: Response):
    """Checks result by its query_id"""
    if check_task_exists(str(data.query_id)):
        task = AsyncResult(id=str(data.query_id), app=celery)
        task_status = task.status
        if task.status == 'SUCCESS':
            return task.result
        return {'result': task_status}
    response.status_code = status.HTTP_406_NOT_ACCEPTABLE
    return {'result': 'this query_id doesn\'t exist'}


@router.get('/ping', response_model=PingResp)
async def ping():
    """Returns server status"""
    return {"server_status": "ok"}
