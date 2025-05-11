import uvicorn
from fastapi import FastAPI, Query
from typing import Optional
from datetime import date

app = FastAPI()


@app.get("/hotels/{hotel_id}")
async def get_hotel(
                    date_from: date,
                    date_to: date,
                    location: str,
                    rating: Optional[int] = Query(None, ge=1, le=5),
                    has_spa: Optional[bool] = None,):
    return {"location": location  ,
            "date_from": date_from,
            "date_to": date_to,
            "rating": rating,
            "has_spa": has_spa,
            "result": "success"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
