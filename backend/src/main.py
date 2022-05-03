from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter

class Photos(BaseModel):
    id: int
    color: str
    mass: float

app = FastAPI(
        title="Album dinamico",
        description="Testando umas paradinhas maneiras",
        version="0.0.0.1",
    )
router = MemoryCRUDRouter(schema=Photos)
app.include_router(router)

@app.get("/")
def read_root():
    return {"It's Working | version 0.0.0.1"}