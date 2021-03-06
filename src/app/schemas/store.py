from typing import List

from pydantic import BaseModel

from app.schemas.base import BaseHttpResponse


class StoreResponseDto(BaseModel):
    id: int
    name: str
    long: float
    lat: float
    view_count: int
    image: str = ""


class StoreResponse(BaseHttpResponse):
    data: List[StoreResponseDto]
