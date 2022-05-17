import unittest

from app.db.session import SessionLocal
from app.models.category import Category

from app.db.db_setup import create_db, drop_db


class TestCategory(unittest.TestCase):
    def setUp(self):
        create_db()
        self.session = SessionLocal()

    def test_category(self):
        # 카테고리 데이터 생성
        category = Category("restaurant", "17849")

        self.session.add(category)
        self.session.commit()
        self.session.close()

        # 카테고리 데이터 조회
        category = self.session.query(Category).all()[-1]
        self.session.close()

        self.assertEqual(category.name, "restaurant")
        self.assertEqual(category.code, "17849")

    def tearDown(self) -> None:
        drop_db()
