# boiler plate for fastapi

from fastapi import FastAPI
import uvicorn
from mongodb import MongodbHelper
from mongodb_models import Note_Item

app = FastAPI()
mongodb_helper = MongodbHelper()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, query: str = None):
    return {"item_id": item_id, "query": query}

@app.post("/items/")
async def create_item(item: Note_Item):
    mongodb_helper.insert_one(item.model_dump())
    return item


if __name__ == "__main__":
    uvicorn.run(app, debug=True)