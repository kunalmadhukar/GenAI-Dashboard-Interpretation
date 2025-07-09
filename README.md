# GenAI Dashboard

This project provides a minimal full‑stack template for building a dashboard that interacts with generative AI services. The repository is organised into separate **backend**, **frontend** and **docker** folders.

## Project Structure

```
backend/   - FastAPI application with OpenAI integration
frontend/  - React + Vite user interface
docker/    - Docker compose and ignore files
```

## Backend

The backend is a small FastAPI service. Dependencies are declared in `backend/requirements.txt` and the service is started with Uvicorn. A `.env` file (not committed) should contain your OpenAI credentials:

```
OPENAI_API_KEY=your_openai_key_here
```

To build and run just the backend container:

```bash
docker build -t genai-backend ./backend
```

The `backend/Dockerfile` has been updated so all copies use paths relative to the Docker build context.

## Frontend

The frontend uses React and Vite. `frontend/package.json` defines the minimal dependencies. The example `index.html` and `src/main.jsx` were generated with `yarn create vite`.

To start the development server locally:

```bash
cd frontend
yarn install
yarn start
```

## Docker Compose

`docker/docker-compose.yml` can be used to run both services together:

```bash
docker compose -f docker/docker-compose.yml up --build
```

## AWS Deployment

Images can be pushed to AWS ECR and run on ECS (Fargate) or an EC2 instance using Docker Compose. Configure an ALB with two target groups – one for the frontend on port **3000** and another for the backend on port **8000**.

Optional CI/CD can be achieved via GitHub Actions that authenticate to AWS and push updated images.

