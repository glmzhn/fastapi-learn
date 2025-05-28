import uvicorn
from fastapi import FastAPI, Depends
from schemas import BookingSchema, HotelSchema
from query_params import HotelQueryParams

app = FastAPI()


@app.get("/hotels", response_model=list[HotelSchema])
async def get_hotel(query_schema: HotelQueryParams = Depends()):

    mock_data = [
        {
            "address": "Gagarin Street 12, Almaty",
            "name": "Pushkin Hotel",
            "rating": 3
        },
        {
            "address": "Al-Farabi Street 4/1, Almaty",
            "name": "Abay Hotel",
            "rating": 5
        }
    ]

    hotels_result: list[HotelSchema] = []

    for hotel in mock_data:
        hotels_result.append(HotelSchema(**hotel))

    return hotels_result


@app.post("/bookings")
async def add_booking(booking: BookingSchema):
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
