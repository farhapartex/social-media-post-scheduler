# tests/test_posts.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_scheduled_posts():
    response = client.get("/posts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test fetching a single post by ID
def test_get_post_by_id():
    # Assuming we are testing with ID = 1
    response = client.get("/posts/1")
    if response.status_code == 200:
        post = response.json()
        assert "id" in post
        assert "content" in post
    else:
        assert response.status_code == 405  # Post not found
