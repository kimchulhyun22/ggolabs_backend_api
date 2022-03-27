from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry

Base = declarative_base()


class Place(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    location = Column(Geometry('POINT'), index=True)

