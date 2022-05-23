from app.db.session import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from geoalchemy2 import Geometry
from app.models.category import Category


class Store(Base):
    __tablename__ = "store"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    location = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    image = Column(String(200), nullable=True)
    view_count = Column(Integer, nullable=False, default=0)
    category_id = Column(Integer, ForeignKey('category.id'))

    def __init__(self, name, location, image="", view_count=0):
        self.name = name
        self.location = location
        self.image = image
        self.view_count = view_count
