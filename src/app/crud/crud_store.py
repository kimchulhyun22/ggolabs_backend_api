from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.crud.crud_category import increase_category_viewcount
from app.models.category import Category
from app.models.store import Store
from app.schemas.store import StoreResponseDto
from app.util.data_transform import transform_wkb_element_to_xy

STORE_PAGEINATION = 15


def get_store_list_by_category_id(db: Session, category_id: int, long: float, lat: float,
                                  dist: int, page_num: int) -> List[StoreResponseDto]:
    increase_category_viewcount(db=db, category_id=category_id, count=1)

    store_list = db.query(Store).filter(
        func.ST_DistanceSphere(Store.location, 'POINT({} {})'.format(long, lat)) < dist)\
        .filter_by(category_id=category_id).order_by(Store.view_count.desc()).limit(5)

    store_list = store_list[STORE_PAGEINATION * page_num:STORE_PAGEINATION * (page_num + 1)]
    store_response_dto_list = []

    for store in store_list:
        x, y = transform_wkb_element_to_xy(store.location)

        store_response_dto_list.append(
            StoreResponseDto(id=store.id,
                             name=store.name,
                             long=x,
                             lat=y,
                             view_count=store.view_count,
                             image=store.image))

    return store_response_dto_list
