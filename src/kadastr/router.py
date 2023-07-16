from fastapi import APIRouter, Depends, Response, status
from httpx import AsyncClient, ConnectError

from kadastr.base_config import get_async_client
from kadastr.responses import ext_api_resp, query_resp, result_resp
from kadastr.schemas import (
    PingOptions,
    PingResp,
    QueryGet,
    QueryResp,
    ResultCheckStatus,
    ResultResp,
)
from src.config import EXTERNAL_API

router = APIRouter()


@router.post('/query', response_model=QueryResp, responses=query_resp)
async def query(
    data: QueryGet, client: AsyncClient = Depends(get_async_client)
):
    """Returns query_id from ext API for result checking"""

    try:
        response = await client.post(url='/query', json=dict(data))
        result = response.json()
        id = result.get('query_id')
        return {"query_id": f"{id}"}
    except ConnectError:
        return {'query_id': 'try later, please'}


@router.post('/result', response_model=ResultResp, responses=result_resp)
async def result(
    data: ResultCheckStatus,
    response: Response,
    client: AsyncClient = Depends(get_async_client),
):
    """Checks result by its query_id"""
    try:
        data = {"query_id": f'{data.query_id}'}
        response = await client.post('/result', json=data)
        if response.status_code == status.HTTP_406_NOT_ACCEPTABLE:
            response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return response.json()
    except ConnectError:
        return {'result': 'try later, please'}


@router.get('/ping', response_model=PingResp, responses=ext_api_resp)
async def ping(response: Response):
    """Checks if external API is working"""
    async with AsyncClient(base_url=EXTERNAL_API) as client:
        try:
            serv_response = await client.get('/ping')
            if serv_response.status_code == 200:
                return {'server_status': PingOptions.ok}
        except ConnectError:
            response.status_code = status.HTTP_504_GATEWAY_TIMEOUT
            return {'server_status': PingOptions.disabled}
