import unittest

from app.core.config import settings
from app.db.init_db import drop_db
from app.db.session import SessionLocal
from app.main import app
from fastapi.testclient import TestClient

from app.models.store import Store


class TestCategory(unittest.TestCase):
    def setUp(self) -> None:
        self.test_client = TestClient(app)

        self.test_store = [
            ["matjip1", "POINT(126.5312 33.4996)"],
            ["matjip2", "POINT(126.5312 33.4996)"],
            ["matjip3", "POINT(126.5312 33.4996)"],
            ["matjip4", "POINT(126.5312 33.4996)"]
        ]

    def test_category_list(self):
        response = self.test_client.get(f"{settings.API_V1_PREFIX}/categories")
        response_json = response.json()

        self.assertEqual(response.status_code, 200)
        # 결과가 빈 값인 경우
        self.assertNotEqual(response_json, None)
        self.assertNotEqual(response_json, [])

        # 필드 체크
        response_first, response_second = response_json[0], response_json[1]

        self.assertEqual('id' in response_first, True)
        self.assertEqual('name' in response_first, True)
        self.assertEqual('view_count' in response_first, True)
        self.assertEqual('image' in response_first, True)

        self.assertEqual('id' in response_second, True)
        self.assertEqual('name' in response_second, True)
        self.assertEqual('view_count' in response_second, True)
        self.assertEqual('image' in response_second, True)

        self.assertEqual(response_first['view_count'] >= response_second['view_count'], True)

    def test_store_list(self):
        session = SessionLocal()

        for store_name, store_location in self.test_store:
            store = Store(name=store_name,
                          location=store_location)
            store.category_id = 1
            session.add(store)
            session.commit()

        session.close()

        response = self.test_client.get(f"{settings.API_V1_PREFIX}/categories/1/stores")
        response_json = response.json()
        response_json = response_json["data"]

        self.assertEqual(response.status_code, 200)

        # 결과가 빈 값인 경우
        self.assertNotEqual(response_json, None)
        self.assertNotEqual(response_json, [])

        # 필드 체크
        self.assertEqual("id" in response_json[0], True)
        self.assertEqual("name" in response_json[0], True)
        self.assertEqual("x" in response_json[0], True)
        self.assertEqual("y" in response_json[0], True)
        self.assertEqual("view_count" in response_json[0], True)
        self.assertEqual("image" in response_json[0], True)

    def tearDown(self) -> None:
        drop_db()
