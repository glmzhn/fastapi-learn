import uvicorn
from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from schemas import BookingSchema, HotelSchema

app = FastAPI()


@app.get("/hotels/{hotel_id}", response_model=list[HotelSchema])
async def get_hotel(
                    date_from: date,
                    date_to: date,
                    location: str,
                    rating: Optional[int] = Query(None, ge=1, le=5),
                    has_spa: Optional[bool] = None,):

    mock_data = [
        {
            "address": "Almaty, Gagarin street, 12",
            "name": "Pushkin Hotel",
            "rating": 3,
        },
        {
            "address": "Almaty, Al-Farabi street, 23/1",
            "name": "Abay Hotel",
            "rating": 4,
        },
    ]

    hotels_list: list[HotelSchema] = []
    for hotel in mock_data:
        hotels_list.append(HotelSchema(**hotel))

    return hotels_list


@app.post("/bookings")
async def add_booking(booking: BookingSchema):
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
