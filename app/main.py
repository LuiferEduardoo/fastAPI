from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import init_db

app = FastAPI(lifespan=init_db)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hola Mundo desde FastAPI"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
