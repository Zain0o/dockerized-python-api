import pytest
from app import app as flask_app

@pytest.fixture
def app():
    # --- The Magic Happens Here ---
    # Use monkeypatch to fake the environment variables
    # This prevents the app from trying to connect to a real database
    pytest.monkeypatch.setenv("POSTGRES_USER", "testuser")
    pytest.monkeypatch.setenv("POSTGRES_PASSWORD", "testpass")
    pytest.monkeypatch.setenv("POSTGRES_HOST", "localhost")
    pytest.monkeypatch.setenv("POSTGRES_DB", "testdb")

    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_tasks_returns_ok(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/tasks' page is requested (GET)
    THEN check that the response is valid (200 OK)
    """
    # We will also mock the database call itself to avoid any connection
    # This is a more robust way to unit test
    with pytest.MonkeyPatch.context() as m:
        # Pretend Task.query.all() returns an empty list
        m.setattr("app.Task.query.all", lambda: [])
        response = client.get('/tasks')

    assert response.status_code == 200