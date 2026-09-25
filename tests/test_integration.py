from fastapi.testclient import TestClient

from service import app


def test_http_contract_and_domain():
    c = TestClient(app)
    assert c.get("/health/live").status_code == 200
    r = c.post(
        "/v1/deployments",
        json={
            "key": "integration",
            "payload": {"image": "example:latest", "replicas": 2},
        },
    )
    assert r.status_code == 200, r.text
