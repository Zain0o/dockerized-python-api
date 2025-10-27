# Dockerized Python To-Do API

This project is a simple RESTful API for a To-Do list, built with Python and Flask. The entire application stack, including the PostgreSQL database, is fully containerized using Docker and orchestrated with Docker Compose.

The primary goal of this project is to demonstrate foundational knowledge of containerization, multi-container networking, and data persistence in a real-world developer workflow.

## Skills Demonstrated

*   **Containerization:** Creating a clean, efficient Docker image for a Python application using a `Dockerfile`.
*   **Orchestration:** Using `docker-compose.yml` to define and run a multi-container application (API + Database).
*   **Networking:** Establishing a network bridge between the application container and the database container, allowing them to communicate by service name.
*   **Data Persistence:** Using Docker Volumes to persist PostgreSQL data, ensuring that data is not lost when containers are stopped or removed.
*   **Dependency Management:** Solving container startup order issues with Docker Compose `healthcheck` to ensure the application only starts after the database is fully ready.
*   **Backend Development:** A simple REST API built with Python and Flask.

## Prerequisites

*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

## How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/dockerized-python-api.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd dockerized-python-api
    ```

3.  **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```
    The application will be available on `http://localhost:5001`.

## API Usage

You can use `curl` or any API client (like Postman) to interact with the API.

#### 1. Create a new task

```bash
curl -X POST http://localhost:5001/tasks \
     -H "Content-Type: application/json" \
     -d '{"description": "Showcase my Docker skills"}'
