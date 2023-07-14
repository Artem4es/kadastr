from celery.result import AsyncResult
from fastapi import APIRouter, Response, status
from httpx import AsyncClient

from kadastr.responses import ext_api_resp
from kadastr.schemas import (
    PingResp,
    QueryGet,
    QueryResp,
    ResultCheckStatus,
    ResultResp,
)
from src.config import EXTERNAL_API
from tasks.tasks import celery, get_response
from tasks.utils import check_task_exists, set_task

router = APIRouter()


@router.post('/query', response_model=QueryResp)
async def query(
    data: QueryGet,
):
    """Returns query_id for result checking"""
    task_id = get_response.delay(dict(data)).id
    set_task(str(task_id))
    print(task_id)
    return {"query_id": f"{task_id}"}


@router.post('/result', response_model=ResultResp)
async def result(data: ResultCheckStatus):
    """Checks result by its query_id"""
    if check_task_exists(str(data.query_id)):
        task = AsyncResult(id=str(data.query_id), app=celery)

        status = task.status
        if task.status == 'SUCCESS':
            return task.result
        return {'result': status}
    return {'result': 'this query_id doesn\'t exist'}


@router.get('/ping', response_model=PingResp, responses=ext_api_resp)
async def ping(response: Response):
    """Checks if external API is working"""
    async with AsyncClient(base_url=EXTERNAL_API) as client:
        serv_response = await client.get('/ping')
        if serv_response.status_code == 200:
            return {'server_status': 'ok'}
        response.status_code = status.HTTP_504_GATEWAY_TIMEOUT
        return {'server_status': 'disabled'}
