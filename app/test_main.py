from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_create_short_url():
    mock_url = {
        "url": "https://fondeadora.com/"
    }
    response = client.post("/", json=mock_url)
    assert response.status_code == 200
    assert response.json().get("short_url")


def test_get_original_url():
    mock_url = {
        "url": "https://fondeadora.com/"
    }
    response_url = client.post("/", json=mock_url)
    code = response_url.json().get("short_url")

    response = client.get(f'{code}')

    assert response.status_code == 200
    assert response.json().get("url") == mock_url.get('url')


def test_looking_with_wrong_code():
    response = client.get('/WroNGcoDe')

    assert response.status_code == 404
    assert response.json().get("detail") == "Not found"
