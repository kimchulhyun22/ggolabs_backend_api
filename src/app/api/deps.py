from typing import Generator

from app.db.session import SessionLocal


def get_db_session() -> Generator:
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
