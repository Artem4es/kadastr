from typing import Union
from uuid import UUID

from pydantic import BaseModel, confloat, constr


class QueryGet(BaseModel):
    """Input data from client"""

    kad_number: constr(
        pattern=r'^\d{2}:\d{2}:\d{7}:\d{4}$'
    )  # Добавить кастомную ошибку
    lat: confloat(ge=-90, le=90)
    long: confloat(ge=-180, le=180)


class QueryResp(BaseModel):
    """Return task UUID to client"""

    query_id: UUID


class ResultCheckStatus(BaseModel):
    """Input query id from client"""

    query_id: UUID


class ResultResp(BaseModel):
    """Return result or status to client"""

    result: Union[bool, str]


class PingResp(BaseModel):
    """Model for server status endpoint"""

    server_status: str
