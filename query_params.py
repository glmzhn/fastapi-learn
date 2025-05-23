from fastapi import Query
from datetime import date
from typing import Optional


class HotelQueryParams:
    def __init__(
        self,
        date_from: date = Query(description="Date of Arrival (YYYY-MM-DD)"),
        date_to:   date = Query(description="Date of Departure (YYYY-MM-DD)"),
        location:  str  = Query(description="Location"),
        rating:    Optional[int]  = Query(None, ge=1, le=5, description="Rating 1–5"),
        has_spa:   Optional[bool] = Query(None, description="Has spa (true/false)"),
    ):

        self.date_from = date_from
        self.date_to   = date_to
        self.location  = location
        self.rating    = rating
        self.has_spa   = has_spa
