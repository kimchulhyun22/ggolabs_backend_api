from app.db.session import Base, engine
from sqlalchemy import Column, Integer, String


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    code = Column(String(50), nullable=False)

    def __init__(self, name, code):
        self.name = name
        self.code = code
        