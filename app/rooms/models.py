from app.database import Base
from sqlalchemy import Column, Integer, String, JSON, Float, ForeignKey


class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(ForeignKey("hotels.id"), index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    services = Column(JSON)
    quantity = Column(Integer)
    image_id = Column(Integer)
