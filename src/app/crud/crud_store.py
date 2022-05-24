from typing import List

from sqlalchemy.orm import Session

from app.models.store import Store
from app.schemas.store import StoreResponseDto
from app.util.data_transform import transform_wkb_element_to_xy


def get_store_list_by_category_id(db: Session, category_id: int) -> List[StoreResponseDto]:
    store_list = db.query(Store).filter_by(category_id=category_id).order_by(Store.view_count.desc()).all()
    store_response_dto_list = []

    for store in store_list:
        x, y = transform_wkb_element_to_xy(store.location)

        store_response_dto_list.append(
            StoreResponseDto(id=store.id,
                             name=store.name,
                             x=x,
                             y=y,
                             view_count=store.view_count,
                             image=store.image))

    return store_response_dto_list
