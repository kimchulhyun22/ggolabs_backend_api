from app.db.session import Base
from sqlalchemy import Column, Integer, String


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    image = Column(String(200), nullable=True)
    code = Column(String(50), nullable=True)
    view_count = Column(Integer, default=0)

    def __init__(self, name, image=None, code="", view_count=None):
        self.name = name
        self.code = code
        self.view_count = view_count
        self.image = image
