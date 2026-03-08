from fastapi import FastAPI
from .database import engine, Base
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
