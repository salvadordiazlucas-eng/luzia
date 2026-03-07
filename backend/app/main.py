from fastapi import FastAPI

app = FastAPI(
    title="LUZÍA API",
    description="Sistema inteligente de gestión de reservas para restaurantes",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "LUZÍA API funcionando correctamente"}
