from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Float, Computed


class Bookings(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(ForeignKey("rooms.id"))
    user_id = Column(ForeignKey("users.id"))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    daily_price = Column(Float, nullable=False)
    total_days = Column(Integer, Computed("(date_to - date_from)"))
    total_cost = Column(Float, Computed("((date_to - date_from) * daily_price)"))
