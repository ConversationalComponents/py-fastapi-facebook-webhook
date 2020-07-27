from fastapi.testclient import TestClient
from ..main import app


client = TestClient(app)


def test_verification():
    """
    Test webhook verification mechanism.
    """
    challenge_value = "challenge"

    response = client.get("/api/webhook", params={
        "hub.mode": "subscribe",
        "hub.verify_token": "test",  ## Must match the VERIFY_TOKEN env variable.
        "hub.challenge": challenge_value
    })
    assert response.status_code == 200
    assert response.content == challenge_value
