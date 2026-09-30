from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_app_has_expected_title() -> None:
    assert app.title == "FastAPI Boilerplate"


def test_health_endpoint_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert response.headers["content-type"].startswith("application/json")


def test_health_endpoint_is_exposed_in_openapi() -> None:
    response = client.get("/openapi.json")

    assert response.status_code == 200
    health_operation = response.json()["paths"]["/health"]["get"]
    assert health_operation["tags"] == ["health"]
    assert health_operation["responses"]["200"]["description"] == "Successful Response"


def test_unknown_endpoint_returns_not_found() -> None:
    response = client.get("/not-found")

    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_health_endpoint_rejects_unsupported_method() -> None:
    response = client.post("/health")

    assert response.status_code == 405