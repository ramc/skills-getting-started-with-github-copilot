from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_delete_participant_removes_email_from_activity():
    response = client.delete(
        "/activities/Chess%20Club/participants/michael@mergington.edu"
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["message"] == "Removed michael@mergington.edu from Chess Club"

    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
