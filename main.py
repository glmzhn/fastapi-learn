import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/hotels/{hotel_id}")
async def get_hotel(hotel_id: int, date_from, date_to):
    return {"hotel_id": hotel_id, "date_from": date_from, "date_to": date_to, "result": "success"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
