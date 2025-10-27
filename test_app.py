import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_tasks_returns_ok(client):
    """
    GIVEN a Flask application
    WHEN the '/tasks' page is requested (GET)
    THEN check that the response is valid (200 OK)
    """
    response = client.get('/tasks')
    assert response.status_code == 200