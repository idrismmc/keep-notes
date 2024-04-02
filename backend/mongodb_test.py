from mongodb import MongodbHelper
import pytest
from mongomock import MongoClient

@pytest.fixture
def mongodb_helper():
    helper = MongodbHelper()
    helper.client = MongoClient()
    return helper
    
def test_insert_one(mongodb_helper):
    data = {"name": "test"}
    inserted_id = mongodb_helper.insert_one(data)
    assert inserted_id is not None

def test_find_one(mongodb_helper):
    query = {"name": "test"}
    data = {"name": "test"}
    mongodb_helper.insert_one(data)
    result = mongodb_helper.find_one(query)
    assert result is not None
    assert result["name"] == "test"

def test_delete_one(mongodb_helper):
    query = {"name": "test"}
    data = {"name": "test"}
    mongodb_helper.insert_one(data)
    result = mongodb_helper.delete_one(query)
    assert result.deleted_count == 1

def test_drop_collection(mongodb_helper):
    data = {"name": "test"}
    mongodb_helper.insert_one(data)
    result = mongodb_helper.drop_collection()
    assert result is None

def test_update_one(mongodb_helper):
    query = {"name": "test"}
    data = {"name": "test"}
    mongodb_helper.insert_one(data)
    update_data = {"$set": {"name": "updated"}}
    result = mongodb_helper.update_one(query, update_data)
    assert result.modified_count == 1
    updated_query = {"name": "updated"}
    updated_result = mongodb_helper.find_one(updated_query)
    assert updated_result is not None
    assert updated_result["name"] == "updated"