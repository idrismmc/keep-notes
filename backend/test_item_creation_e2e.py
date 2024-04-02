# End to end item creation test
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
async def test_item_creation_e2e(test_client, mongodb_helper):
    item = Note_Item(title="test", description="test", priority=1, completed=False)
    response = test_client.post("/items/", json=item.model_dump())
    assert response.status_code == 200
    assert response.json() == item.model_dump()
    result = mongodb_helper.find_one({"title": "test"})
    assert result is not None
    assert result["title"] == "test"



    