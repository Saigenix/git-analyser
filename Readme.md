# Autonomous Code Review Agent

This project implements an autonomous code review agent system that uses AI to analyze GitHub pull requests. It performs asynchronous code analysis using Celery, FastAPI, Redis, and a chosen AI language model (e.g., Gemini). The agent can identify code style issues, potential bugs, performance improvements, and best practices in code.

## Features

- **API Endpoints**:
  - `POST /analyze-pr`: Analyze a GitHub pull request.
  - `GET /status/<task_id>`: Check the status of an analysis task.
  - `GET /results/<task_id>`: Retrieve analysis results.
- **Asynchronous Processing**: Celery is used to handle analysis tasks asynchronously.
- **AI-Driven Code Analysis**: The AI agent reviews code for style, bugs, performance, and best practices.
- **Docker-Compose Deployment**: Supports easy setup and teardown with Docker Compose.

---

## Prerequisites

- **Docker and Docker Compose** (if using Docker)
- **Python 3.8+** (if running locally)

## Setup and Run

### Method 1: Using Docker Compose

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Build and Start the Services**:
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**:
   - FastAPI will be available at `http://localhost:8000`.
   - You can interact with the API using the endpoints listed below.

4. **Shut Down the Services**:
   ```bash
   docker-compose down
   ```

### Method 2: Running Locally Without Docker

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Activate the virtual environment
   pip install -r requirements.txt
   ```

3. **Start Redis**:
   Make sure Redis is running on your machine (default port `6379`). You can install Redis locally or use Docker to run a Redis container:
   ```bash
   docker run -d -p 6379:6379 redis
   ```

4. **Start Celery Worker**:
   In one terminal, start the Celery worker:
   ```bash
   celery -A app.tasks worker --loglevel=info
   ```

5. **Start FastAPI Application**:
   In another terminal, start the FastAPI app:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

6. **Access the Application**:
   - The application will be available at `http://localhost:8000`.

---

## API Documentation

Once the app is running, you can access the interactive API documentation at `http://localhost:8000/docs`.

### Endpoints

1. **Analyze Pull Request**:
   - **Endpoint**: `POST /analyze-pr`
   - **Description**: Analyze a GitHub pull request.
   - **Payload**:
     ```json
     {
       "repo": "https://github.com/owner/repo-name",
       "pr_number": 1
     }
     ```
   - **Response**: Returns a task ID to track the analysis status.

2. **Check Task Status**:
   - **Endpoint**: `GET /status/<task_id>`
   - **Description**: Check the current status of a task.
   - **Response**: Returns the status (e.g., pending, processing, completed).

3. **Retrieve Analysis Results**:
   - **Endpoint**: `GET /results/<task_id>`
   - **Description**: Retrieve the results of an analysis task.
   - **Response**: JSON object containing the code review analysis.

---

## Configuration

Set the following environment variables in your `.env` file or Render configuration (if deploying):

- `CELERY_BROKER_URL`: URL of the Redis server, e.g., `redis://localhost:6379/0`
- `CELERY_RESULT_BACKEND`: URL of the Redis server, e.g., `redis://localhost:6379/0`
- `API_KEY` : Your gemini api key
---

## Future Improvements

- **Add support for multiple programming languages** in code analysis.
- **Implement caching** to avoid duplicate processing for the same pull request.
- **Enhance error handling** and logging for better debugging and monitoring.
- **Deploy on Render or another cloud platform** for a production-ready setup.

---

## License

This project is licensed under the MIT License.
