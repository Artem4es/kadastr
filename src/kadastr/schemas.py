from enum import Enum
from typing import Union
from uuid import UUID

from pydantic import BaseModel


class QueryGet(BaseModel):
    """Input data from client"""

    kad_number: str  # может валидацию прикрутить может уже есть нужный тип??
    alt: float  # пропускает integer  может уже есть нужный тип??
    long: float


class QueryResp(BaseModel):
    """Response to client"""

    query_id: UUID


class ResultCheckStatus(BaseModel):
    """Input query id from client"""

    query_id: UUID


class ResultResp(BaseModel):
    """Response status to client"""

    result: Union[bool, str]


class PingOptions(str, Enum):
    ok = 'ok'
    disabled = 'disabled'


class PingResp(BaseModel):  # Enum?
    """Ping response model"""

    server_status: str
