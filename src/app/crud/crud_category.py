from typing import List

from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryResponseDto


def get_category_list_sorted_by_view_count(db: Session) -> List[CategoryResponseDto]:
    category_list = db.query(Category).order_by(Category.view_count.desc()).all()

    return [
        CategoryResponseDto(id=category.id,
                            name=category.name,
                            view_count=category.view_count,
                            image=category.image) for category in category_list]


def increase_category_viewcount(db: Session, category_id: int, count: int):
    category = db.query(Category).filter_by(id=category_id).one()
    category.view_count += 1
    db.commit()
    db.close()
