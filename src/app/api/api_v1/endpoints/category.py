from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.crud.crud_category import get_category_list_sorted_by_view_count
from app.schemas.category import CategoryResponse

router = APIRouter()


@router.get("")
def get_category_list(db: Session = Depends(get_db_session)) -> Any:
    category_list = get_category_list_sorted_by_view_count(db=db)

    return CategoryResponse(
        status_code=200,
        data=[
            category.__dict__ for category in category_list
        ]
    )
