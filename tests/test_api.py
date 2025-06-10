import pytest

from fastapi.testclient import TestClient

from src.api.routes import app

client = TestClient(app)


def test_predict_endpoint_return_200():
    response = client.post("/predict", json={"features": [0.1] * 7})
    assert response.status_code == 200
    assert "pm25" in response.json()


def test_predict_endpoint_return_value_error():
    with pytest.raises(ValueError) as exc_info:
        client.post("/predict", json={"features": [0.1] * 5})

    # Optional: assert on the exception message
    assert "Expected exactly 7 input features" in str(exc_info.value)
    assert "got 5" in str(exc_info.value)
