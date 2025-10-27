import pytest
from app import app as flask_app, db as _db

# This fixture sets up the application for all tests
@pytest.fixture(scope='module')
def app():
    # Set up a test configuration
    flask_app.config.update({
        "TESTING": True,
        # Use an in-memory SQLite database for tests to be fast and isolated
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    # Create the database and the database table(s)
    with flask_app.app_context():
        _db.create_all()

    yield flask_app

    # Tear down the database
    with flask_app.app_context():
        _db.drop_all()

# This fixture gives us a client to make requests to the app
@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

# The actual test function
def test_get_tasks_returns_ok(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/tasks' page is requested (GET)
    THEN check that the response is valid (200 OK)
    """
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json == [] # Check that it returns an empty list