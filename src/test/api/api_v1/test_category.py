import unittest

from app.core.config import settings
from app.main import app
from fastapi.testclient import TestClient


class TestCategory(unittest.TestCase):
    def setUp(self) -> None:
        self.test_client = TestClient(app)

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
