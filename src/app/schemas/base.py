from typing import Optional

from pydantic import BaseModel


class BaseHttpResponse(BaseModel):
    status_code: int
    error_message: Optional[str] = ""
