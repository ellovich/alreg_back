import uvicorn
from fastapi import FastAPI

from src.config import settings

app = FastAPI(
    title="Регистр Алмазова"
)

@app.get("/")
def hello_world():
    return f"HELLO"
