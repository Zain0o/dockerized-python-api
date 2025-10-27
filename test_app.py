import pytest
from app import app as flask_app

# The 'app' fixture now requests the 'monkeypatch' fixture as an argument.
@pytest.fixture
def app(monkeypatch):
    # Now we use the 'monkeypatch' object that pytest provided.
    monkeypatch.setenv("POSTGRES_USER", "testuser")
    monkeypatch.setenv("POSTGRES_PASSWORD", "testpass")
    monkeypatch.setenv("POSTGRES_HOST", "localhost")
    monkeypatch.setenv("POSTGRES_DB", "testdb")

    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

# The test function itself also requests the 'monkeypatch' fixture.
def test_get_tasks_returns_ok(client, monkeypatch):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/tasks' page is requested (GET)
    THEN check that the response is valid (200 OK)
    """
    # We use the provided monkeypatch object to mock the database call.
    # No 'with' statement is needed.
    monkeypatch.setattr("app.Task.query.all", lambda: [])
    response = client.get('/tasks')

    assert response.status_code == 200