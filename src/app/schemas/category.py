from typing import Optional, List

from pydantic import BaseModel
from app.schemas.base import BaseHttpResponse


class CategoryResponseDto(BaseModel):
    id: int
    name: str
    view_count: int
    image: Optional[str] = ""


class CategoryResponse(BaseHttpResponse):
    data: List[CategoryResponseDto]
