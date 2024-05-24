from enum import StrEnum
from datetime import datetime

from pydantic import BaseModel, model_validator


class Book(BaseModel):
    name: str
    author: str
    publish_date: datetime
    price_rub: int
    genre: str
    publishing_house: str


class Status(StrEnum):
    created = 'created'
    waiting = 'waiting'
    finished = 'finished'


class DeliveryRequest(BaseModel):
    pay_first: bool = True
    address: str
    time: datetime


class RefundRequest(BaseModel):
    address: str | None = None
