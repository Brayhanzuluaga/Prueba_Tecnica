#import logging
from fastapi import FastAPI
from app.Events import routers
from app.Events.repository import create_tables


# Funcion de creacion de las tablas en la base de datos
create_tables()

app = FastAPI(prefix="/main",
              tags=["main"],
              responses={404: {
                  "Message": "No encontrado "
              }})

# Routers
app.include_router(routers.router)


@app.get("/")
async def root():
    """
    Peticion Get principal.
    """
    return {
        "message": "Api funcionando correctamente",
        "Link del repositorio": "https://github.com/Brayhanzuluaga"
    }


# uvicorn main:app --reload
