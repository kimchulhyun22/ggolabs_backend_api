import unittest

from shapely import wkb
from app.db.session import SessionLocal
from app.models.store import Store

from app.db.db_setup import create_db, drop_db


class TestCategory(unittest.TestCase):
    def setUp(self):
        create_db()
        self.session = SessionLocal()

    def test_store(self):
        store = Store(name='matjip',
                      location='POINT(126.5312 33.4996)')

        self.session.add(store)
        self.session.commit()
        self.session.close()

        store = self.session.query(Store).all()[-1]
        self.session.close()

        # WKBElement 데이터 타입 변환
        wkb_data = wkb.loads(bytes(store.location.data))
        x, y = wkb_data.x, wkb_data.y

        self.assertEqual(store.name, 'matjip')
        self.assertEqual(x, 126.5312)
        self.assertEqual(y, 33.4996)

