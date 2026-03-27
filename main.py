from fastapi import FastAPI

app = FastAPI(
    title="Mi API con FastAPI",
    description="Una API REST construida con FastAPI",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Hola Mundo desde FastAPI"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
