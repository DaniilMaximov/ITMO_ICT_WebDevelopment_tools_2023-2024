from typing import List

from sqlmodel import SQLModel, Field, Relationship

from models.trip_models import Trip


class TransportDefault(SQLModel):
    name: str
    description: str
    avalible_seats: int
    price: int

class Transport(TransportDefault, table=True):
    id: int = Field(default=None, primary_key=True)
    trips: List["Trip"] = Relationship(back_populates="transport")