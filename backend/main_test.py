from mongodb import MongodbHelper
import pytest
from mongomock import MongoClient
from fastapi.testclient import TestClient
from main import app
from mongodb_models import Note_Item

@pytest.fixture
def mongodb_helper():
    helper = MongodbHelper()
    helper.client = MongoClient()
    return helper

@pytest.fixture
def test_client():
    return TestClient(app)

@pytest.mark.asyncio
async def test_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_post_item(test_client):
    item = Note_Item(title="test", description="test", priority=1, completed=False)
    response = test_client.post("/items/", json=item.model_dump())
    assert response.status_code == 200
    assert response.json() == item.model_dump()