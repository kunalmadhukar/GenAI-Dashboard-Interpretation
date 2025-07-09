from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["message"] == "GenAI Dashboard API is up"


def test_explanation():
    payload = {"rule_id": "R123", "timestamp": "2025-07-09T12:00:00Z"}
    resp = client.post("/explanation", json=payload)
    assert resp.status_code == 200
    assert "Stub explanation" in resp.json()["message"]


def test_recommend_threshold():
    payload = {"metric_name": "CPU", "window": "7d"}
    resp = client.post("/recommend-threshold", json=payload)
    assert resp.status_code == 200
    assert "recommended_threshold" in resp.json()


def test_rule_hit_summary():
    payload = {"start_date": "2025-07-01", "end_date": "2025-07-08"}
    resp = client.post("/rule-hit-summary", json=payload)
    assert resp.status_code == 200
    assert "Hits from" in resp.json()["summary"]
