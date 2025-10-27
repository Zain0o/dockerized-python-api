# app.py

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the database extension, but don't attach it to an app yet.
db = SQLAlchemy()

def create_app(test_config=None):
    """Application factory function."""
    app = Flask(__name__)

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        db_user = os.environ.get('POSTGRES_USER')
        db_password = os.environ.get('POSTGRES_PASSWORD')
        db_host = os.environ.get('POSTGRES_HOST')
        db_name = os.environ.get('POSTGRES_DB')
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the app with the extension
    db.init_app(app)

    # --- Database Model (needs to be inside the factory or imported) ---
    class Task(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        description = db.Column(db.String(200), nullable=False)

        def to_dict(self):
            return {"id": self.id, "description": self.description}

    # --- API Routes ---
    @app.route('/tasks', methods=['POST'])
    def create_task():
        data = request.get_json()
        new_task = Task(description=data['description'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks])

    return app


# This part is for running the app directly, e.g., with 'python app.py'
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)