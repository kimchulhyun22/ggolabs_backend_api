from app.db.session import Base, engine
from sqlalchemy import Column, Integer, String


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    code = Column(String(50), nullable=False)
    image = Column(String(200), nullable=True)
    click_count = Column(Integer, default=0)

    def __init__(self, name, code, image=None, click_count=None):
        self.name = name
        self.code = code
        self.click_count = click_count
        self.image = image
