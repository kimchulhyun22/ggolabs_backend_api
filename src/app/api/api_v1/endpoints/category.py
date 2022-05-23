from typing import List, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.crud.crud_category import get_category_list_sorted_by_click_count
from app.schemas.category import CategoryResponse

router = APIRouter()


@router.get("")
def get_category_list(db: Session = Depends(get_db_session)) -> Any:
    category_list = get_category_list_sorted_by_click_count(db=db)

    return [
        category.__dict__ for category in category_list
    ]
