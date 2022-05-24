import unittest

from app.crud.crud_store import get_store_list_by_category_id
from app.db.init_db import create_db, drop_db, init_category
from app.db.session import SessionLocal
from app.crud.crud_category import *
from app.models.store import Store


class TestCRUDCategory(unittest.TestCase):
    def setUp(self) -> None:
        create_db()

        self.session = SessionLocal()

        self.session.add(Category(name="맛집"))

        self.test_store = [
            ["matjip1", "POINT(126.5312 33.4996)"],
            ["matjip2", "POINT(126.5312 33.4996)"],
            ["matjip3", "POINT(126.5312 33.4996)"],
            ["matjip4", "POINT(126.5312 33.4996)"]
        ]

    def test_get_store_list_by_category_id(self):
        for store_name, store_location in self.test_store:
            store = Store(name=store_name,
                          location=store_location)
            store.category_id = 1
            self.session.add(store)
            self.session.commit()
        self.session.close()

        store_list = get_store_list_by_category_id(self.session, 1)
        self.session.close()

        for i in range(len(store_list)):
            self.assertEqual(self.test_store[i][0], store_list[i].name)

    def tearDown(self) -> None:
        drop_db()
