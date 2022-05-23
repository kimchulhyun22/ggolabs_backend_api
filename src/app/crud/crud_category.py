from typing import List

from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryResponse


def get_category_list_sorted_by_click_count(db: Session) -> List[CategoryResponse]:
    category_list = db.query(Category).order_by(Category.click_count.desc()).all()

    return [
        CategoryResponse(id=category.id,
                         name=category.name,
                         click_count=category.click_count,
                         image=category.image) for category in category_list]