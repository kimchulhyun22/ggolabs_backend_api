from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.crud.crud_category import get_category_list_sorted_by_view_count
from app.crud.crud_store import store_list_by_category_id
from app.schemas.category import CategoryResponse
from app.schemas.store import StoreResponse

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


@router.get("/{category_id}/stores")
def get_store_list(category_id: int, long: float, lat: float, dist: int, page_num: int,
                   db: Session = Depends(get_db_session)) -> Any:
    store_list = store_list_by_category_id(db=db, category_id=category_id, long=long, lat=lat, dist=dist,
                                           page_num=page_num)

    return StoreResponse(
        status_code=200,
        data=[
            store.__dict__ for store in store_list
        ]
    )
