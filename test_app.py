# test_app.py

import pytest
from app import create_app, db

@pytest.fixture(scope='module')
def app():
    """Instance of Flask app for testing."""
    # Create the app with a specific test configuration
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    # Set up the database context
    with app.app_context():
        db.create_all()

    yield app

    # Clean up the database context
    with app.app_context():
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_get_tasks_returns_ok(client):
    """Test that the /tasks endpoint returns a 200 OK and an empty list."""
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json == []