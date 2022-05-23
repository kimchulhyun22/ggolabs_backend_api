from typing import Optional

from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: int
    name: str
    click_count: int
    image: Optional[str] = ""
