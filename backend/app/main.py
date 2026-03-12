from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, get_db, Base
from . import models


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LUZÍA API",
    description="Sistema inteligente de gestión de reservas para restaurantes",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "LUZÍA API funcionando correctamente"}


@app.post("/restaurants")
def create_restaurant(name: str, db: Session = Depends(get_db)):
    restaurant = models.Restaurant(name=name)
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant


@app.post("/locations")
def create_location(
    restaurant_id: int,
    name: str,
    address: str,
    city: str,
    capacity: int,
    db: Session = Depends(get_db)
):
    location = models.Location(
        restaurant_id=restaurant_id,
        name=name,
        address=address,
        city=city,
        capacity=capacity
    )

    db.add(location)
    db.commit()
    db.refresh(location)

    return location
