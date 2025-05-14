from datetime import date
from pydantic import BaseModel


class BookingSchema(BaseModel):
    room_id: int
    date_from: date
    date_to: date


class HotelSchema(BaseModel):
    address: str
    name: str
    rating: int
