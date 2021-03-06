import json
import os

from .session import Base, engine

from app.db.session import SessionLocal
from app.models.category import Category

session = SessionLocal()


def create_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)


def init_db():
    create_db()

    init_category()


def init_category():
    category_data = None

    file_path = os.path.dirname(__file__)

    with open(file_path + "/../category_data.json", "r") as file:
        category_data = json.load(file)
        category_data = category_data["category"]

    category_list = [category.__dict__ for category in session.query(Category).all()]
    session.close()

    for data in category_data:
        is_find = False

        for category in category_list:
            if data["name"] == category["name"]:
                is_find = True
                break

        if is_find:
            continue

        session.add(Category(
            name=data["name"],
            code=data["code"],
            view_count=data["view_count"],
            image=data["image"]
        ))

        session.commit()

    session.close()
