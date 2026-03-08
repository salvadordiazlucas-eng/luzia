from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, Base, get_db
from . import models

# Crear tablas automáticamente si no existen
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
