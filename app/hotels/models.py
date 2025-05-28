from app.database import Base
from sqlalchemy import Column, Integer, String, JSON


class Hotels(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, index=True, nullable=False)
    services = Column(JSON)
    room_quantity = Column(String, nullable=False)
    image_id = Column(String)
