from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.category import Category


def get_category_list_sorted_by_click_count(db: SessionLocal):
    return db.query(Category).order_by(Category.click_count.desc()).all()
