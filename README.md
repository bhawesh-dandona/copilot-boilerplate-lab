# copilot-boilerplate-lab

Learning repository for GitHub Copilot development, containing a lightweight FastAPI server with a health endpoint and pytest coverage.

## Run locally

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Start the development server:

```powershell
uvicorn app.main:app --reload
```

The health endpoint is available at `http://127.0.0.1:8000/health`. Interactive API docs are at `http://127.0.0.1:8000/docs`.

## Run tests

```powershell
pytest
```

## Run with Docker

```powershell
docker build -t fastapi-boilerplate .
docker run --rm -p 8000:8000 fastapi-boilerplate
```

Then visit `http://127.0.0.1:8000/health`.
