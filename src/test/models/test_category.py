import unittest

from app.db.session import SessionLocal
from app.models.category import Category


class TestCategory(unittest.TestCase):
    def setUp(self):
        from app.db.init import init_db

        init_db()
        self.session = SessionLocal()

    def test_category(self):
        # 카테고리 데이터 생성
        category = Category("restaurant", "17849")

        self.session.add(category)
        self.session.commit()
        self.session.close()

        # 카테고리 데이터 조회
        category = self.session.query(Category).all()[-1]

        self.assertEqual(category.name, "restaurant")
        self.assertEqual(category.code, "17849")

