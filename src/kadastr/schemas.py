from enum import Enum
from typing import Union
from uuid import UUID

from pydantic import BaseModel, confloat, constr


class QueryGet(BaseModel):
    """Input data from client"""

    kad_number: constr(pattern=r'^\d{2}:\d{2}:\d{7}:\d{4}$')
    lat: confloat(ge=-90, le=90)
    long: confloat(ge=-180, le=180)


class QueryResp(BaseModel):
    """Response to client"""

    query_id: Union[UUID, str]


class ResultCheckStatus(BaseModel):
    """Input query id from client"""

    query_id: UUID


class ResultResp(BaseModel):
    """Response status to client"""

    result: Union[bool, str]


class PingOptions(str, Enum):
    """Statuses for ping endpoint"""

    ok = 'ok'
    disabled = 'disabled'


class PingResp(BaseModel):
    """Ping response model"""

    server_status: str
