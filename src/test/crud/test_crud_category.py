import unittest

from app.db.db_setup import create_db, drop_db
from app.db.session import SessionLocal
from app.crud.crud_category import *


class TestCRUDCategory(unittest.TestCase):
    def setUp(self) -> None:
        create_db()
        self.session = SessionLocal()
        self.test_category = [
            "스크린 골프", "카페", "노래방", "펍"
        ]

    def test_category_list_sorted_by_click_count(self):
        # 테스트케이스 인덱스에 따라 클릭 카운트 설정
        for idx, category_name in enumerate(self.test_category):
            self.session.add(Category(category_name, click_count=idx))
            self.session.commit()
        self.session.close()

        category_list = get_category_list_sorted_by_click_count(self.session)
        self.session.close()

        for i in range(len(category_list)):
            self.assertEqual(self.test_category[-i - 1], category_list[i].name)

    def tearDown(self) -> None:
        drop_db()
