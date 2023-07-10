from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.userRoutes import router as userRouter
from routes.rolRoutes import router as rolRouter
from routes.tickerRoutes import router as ticketRouter
from routes.categoriaRoutes import router as CategoriaRouter
from routes.respuestaRoutes import router as RespuestaRouter

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(userRouter, prefix="/user")
app.include_router(rolRouter, prefix="/rol")
app.include_router(ticketRouter, prefix="/ticket")
app.include_router(CategoriaRouter, prefix="/categoria")
app.include_router(RespuestaRouter, prefix="/respuesta")